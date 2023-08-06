import itertools
from collections import defaultdict
from concurrent.futures import Future, ProcessPoolExecutor, as_completed
from pathlib import Path
from typing import Dict, Iterator, List, Set, Tuple, Union

import networkx as nx
import pandas as pd
from typing_extensions import TypeAlias

from pydiscomotif.constants import (AMINO_ACID_ALPHABET,
                                    AMINO_ACID_RELAXED_GROUPS_MAP,
                                    INDEX_ANGLE_BIN_SIZE,
                                    INDEX_DISTANCE_BIN_SIZE)
from pydiscomotif.data_containers import Residue, Residue_pair_data
from pydiscomotif.index_folders_and_files import index_folder_exists
from pydiscomotif.residue_data_dicts import extract_residue_data
from pydiscomotif.utils import (
    angle_between_two_vectors,
    detect_the_compression_algorithm_used_in_the_index, get_bin_number,
    get_sorted_2_tuple, pairwise_euclidean_distance,
    read_compressed_and_pickled_file, sort_and_join_2_strings)


def extract_motif_residues_from_PDB_file(PDB_file: Path, motif: Tuple[str,...]) -> Dict[str, Residue]:
    """
    ...
    """
    residue_data = extract_residue_data(PDB_file)

    motif_residues_data: Dict[str, Residue] = {}
    for residue_ID in motif:
        if residue_ID not in residue_data:
            raise ValueError(f"Could not find residue '{residue_ID}' in PDB_file {str(PDB_file)}.")
        
        motif_residues_data[residue_ID] = residue_data[residue_ID]

    return motif_residues_data

def get_full_residue_ID(residue_ID: str, resname: str) -> str:
    return residue_ID + resname

def get_data_of_all_pairs_of_residues_in_motif(motif_residues_data: Dict[str, Residue]) -> Dict[Tuple[str,str], Residue_pair_data]:
    """
    ...
    """
    data_of_all_pairs_of_residues_in_motif: Dict[Tuple[str,str], Residue_pair_data] = {}
    for (residue_1_ID, residue_1), (residue_2_ID, residue_2) in itertools.combinations(motif_residues_data.items(), 2):
        residue_1_full_ID, residue_2_full_ID = get_full_residue_ID(residue_1_ID, residue_1.resname), get_full_residue_ID(residue_2_ID, residue_2.resname)
        pair_of_residues_full_IDs: Tuple[str,str] = (residue_1_full_ID, residue_2_full_ID) 

        data_of_all_pairs_of_residues_in_motif[pair_of_residues_full_IDs] = Residue_pair_data(
            C_alpha_distance=pairwise_euclidean_distance(residue_1.C_alpha, residue_2.C_alpha), 
            sidechain_CMR_distance=pairwise_euclidean_distance(residue_1.sidechain_CMR, residue_2.sidechain_CMR), 
            vector_angle=angle_between_two_vectors(residue_1.vector, residue_2.vector)
        )

    return data_of_all_pairs_of_residues_in_motif

def get_minimum_spanning_tree(all_pairs_of_residues_data: Dict[Tuple[str,str], Residue_pair_data]) -> nx.Graph:
    """
    Returns the Minimum Spanning Tree (MST) of a motif by creating a dense graph of all the residue pairs in the motif and then applying Kruskal's 
    algorithm using the C alpha distance between the residues. If the motif has 4 residues of less then we don't apply minimum spanning tree and 
    simply return the dense graph, otherwise the graph would not be constrained enough and could result in many false positives. The label
    of the nodes in the graph are full residue IDs, that is '<residue_ID><residue_name>' (ex: 'A12G'), and the edges contain residue pair data.
    """
    graph = nx.Graph()
    for (res1_full_ID, res2_full_ID), residue_pair_data in all_pairs_of_residues_data.items():
        graph.add_edge(
            res1_full_ID, res2_full_ID, 
            weight=residue_pair_data.C_alpha_distance, 
            residue_pair_data=residue_pair_data
        )

    if len(graph) <= 4:
        return graph
    
    minimum_spanning_tree = nx.minimum_spanning_tree(G=graph, algorithm='kruskal')

    return minimum_spanning_tree

def get_nodes_original_residue_map(nodes: List[str]) -> Dict[str,str]:
    # Ex: 'A12P' -> 'A12':'P'
    return {node[:-1]:node[-1] for node in nodes}

def get_nodes_position_specific_exchanges(nodes: List[str], residue_type_policy: Union[str, Dict[str,List[str]]], motif_residues_data: Dict[str, Residue]) -> Dict[str,List[str]]:
    """
    """
    nodes_position_specific_exchanges: Dict[str,List[str]] = {}
    if type(residue_type_policy) is dict:
        for node in nodes:
            node_ID, reference_residue = node[:-1], node[-1]
            if node_ID in residue_type_policy: # The user has specified alternative residues for this residue ID
                alternative_residues: Set[str] = set(residue_type_policy[node_ID])
                alternative_residues.add(reference_residue) # We must also include the original residue as a possibility
                nodes_position_specific_exchanges[node] = [get_full_residue_ID(node_ID, residue) for residue in alternative_residues]

            else: # The user hasn't specified any alternatives, so we only allow the default residue
                nodes_position_specific_exchanges[node] = [node,]

        return nodes_position_specific_exchanges

    elif residue_type_policy == 'relaxed':
        for node in nodes:
            node_ID, reference_residue = node[:-1], node[-1]
            nodes_position_specific_exchanges[node] = [node_ID + residue for residue in AMINO_ACID_RELAXED_GROUPS_MAP[reference_residue]]
        return nodes_position_specific_exchanges

    return nodes_position_specific_exchanges

def get_mutations_mapping(nodes_to_mutate: Tuple[str,...], nodes_original_residue_map: Dict[str,str]) -> Dict[str,str]:
    """
    """
    mutations_mapping = {}
    for node in nodes_to_mutate:
        node_ID = node[:-1] # Ex: 'A12'
        node_original_residue = nodes_original_residue_map[node_ID]
        mutations_mapping[node_ID+node_original_residue] = node
    return mutations_mapping

def get_all_motif_MSTs_generator(motif_MST: nx.Graph, max_n_mutated_residues: int, residue_type_policy: Union[str, Dict[str,List[str]]], motif_residues_data: Dict[str, Residue]) -> Iterator[nx.Graph]:
    """
    ...
    """
    # No mater what, we will always have to solve the initial motif itself, and we can end the generator here if no variants 
    # of the motif need to be generated, ie if we are in 'strict' mode.
    yield motif_MST
    if residue_type_policy == 'strict':
        return

    nodes: List[str] = list(motif_MST.nodes)
    nodes_original_residue_map = get_nodes_original_residue_map(nodes)
    nodes_position_specific_exchanges: Dict[str,List[str]] = get_nodes_position_specific_exchanges(nodes, residue_type_policy, motif_residues_data)
    
    # We only need to check nodes that have more than 1 mutable residue.
    nodes_with_position_specific_exchanges = [node for node, exchanges in nodes_position_specific_exchanges.items() if len(exchanges) > 1]
    if max_n_mutated_residues > len(nodes_with_position_specific_exchanges):
        raise ValueError(f'max_n_mutated_residues was set to {max_n_mutated_residues}, but only {len(nodes_with_position_specific_exchanges)} residues are mutable with the given residue_type_policy.')
    

    for node_combination in itertools.combinations(nodes_with_position_specific_exchanges, max_n_mutated_residues): 
        all_mutations_to_perform: List[List[str]] = [nodes_position_specific_exchanges[node] for node in node_combination]
        for nodes_to_mutate in itertools.product(*all_mutations_to_perform, repeat=1):
            mutated_graph: nx.Graph = nx.relabel_nodes(
                motif_MST, 
                mapping=get_mutations_mapping(nodes_to_mutate, nodes_original_residue_map), 
                copy=True
            )
            
            if mutated_graph.nodes == motif_MST.nodes:
                continue
            
            yield mutated_graph
    
def get_all_pairs_of_residues_to_check(all_motifs_MST: List[nx.Graph]) -> Dict[Tuple[str,str], Residue_pair_data]:
    """
    """
    all_pairs_of_residues_to_check: Dict[Tuple[str,str], Residue_pair_data] = {}
    for MST in all_motifs_MST:
        MST_edges: List[Tuple[str, str]] = list(MST.edges) # Ex: [('A1G', 'A3K'), ('A3K', 'A8N'), ...]

        for pair_of_full_residue_IDs in MST_edges:
            pair_of_full_residue_IDs = get_sorted_2_tuple(pair_of_full_residue_IDs) # Ordering is needed to make sure we only calculate each pair once, ie avoid calculating the results of (A,B) and (B,A), as they are identical.
            if pair_of_full_residue_IDs in all_pairs_of_residues_to_check:
                continue
            
            all_pairs_of_residues_to_check[pair_of_full_residue_IDs] = MST.edges[pair_of_full_residue_IDs]['residue_pair_data']

    return all_pairs_of_residues_to_check

def get_bin_files_to_read(left_bin_number: int, right_bin_number: int, geometric_descriptor_index_folder: Path, pair_of_residues: str, compression: str) -> List[Path]:
    """
    ...
    """
    bin_files_to_read: List[Path] = []
    for bin_number in range(left_bin_number, right_bin_number+1):
        file = geometric_descriptor_index_folder / f'{pair_of_residues}_{bin_number}.{compression}' # Ex: AG_4.bz2
        if file.exists():
            bin_files_to_read.append(file)
    
    return bin_files_to_read

def search_index_for_PDBs_that_contain_the_residue_pair(
        pair_of_residues: str, 
        geometric_descriptor_index_folder: Path,
        value_range: Tuple[float, float],
        compression: str,
    ) -> Dict[str, Set[Tuple[str,str]]]:
    """
    ...
    """
    # All angle values in the index are in the range [0,180], and therefore angles > or < to this range have to be mapped to their corresponding
    # small angle equivalent (ex: 185° -> 175°, 270° -> 90°, ...), but when doing so we can observe that we are guaranteed they will 
    # always be > than the other paired angle in the case of angles > 180°, and vice versa for angles < 0°. Thus we can simply clip the right_value
    # and left_value to 180 and 0 respectively.
    # Angle > 180° example: 175° +/- 10° -> [165, 185] -> We map 185° to 175° -> [165, 180] U [175, 180] == [165, 180]
    # Angle < 180° example:   2° +/- 10° -> [ -8,  12] -> We map  -8° to   8° -> [  0,   8] U [  0,  12] == [  0,  12]
    # Note that the code is also compatible for distances as they must always be positive, and distances > 180 angstroom are forbiden (see input validation)
    left_value, right_value = value_range
    if right_value > 180:
        right_value = 180
    if left_value < 0:
        left_value = 0

    # Only read the files with the bin data of interest.
    bin_size = INDEX_ANGLE_BIN_SIZE if 'angle' in geometric_descriptor_index_folder.name else INDEX_DISTANCE_BIN_SIZE
    left_bin_number, right_bin_number = get_bin_number(left_value, bin_size), get_bin_number(right_value, bin_size)
    bin_files_to_read = get_bin_files_to_read(left_bin_number, right_bin_number, geometric_descriptor_index_folder, pair_of_residues, compression)
    if not bin_files_to_read:
        return {}

    residue_pair_df = pd.concat((read_compressed_and_pickled_file(file) for file in bin_files_to_read), axis=0, copy=False) # Shallow copy is ok in our case, we aren't modifying the data in any way.

    # Use binary search to get the subset of rows in the correct geometric descriptor range. 
    left_index  = residue_pair_df.index.searchsorted(left_value,  'left')
    right_index = residue_pair_df.index.searchsorted(right_value, 'right') # +1 offsetting is taken care of by .searchsorted()

    residue_pair_df = residue_pair_df.iloc[left_index:right_index]

    res1_resname = pair_of_residues[0]
    res2_resname = pair_of_residues[1]
    PDBs_that_contain_the_residue_pair: Dict[str, Set[Tuple[str,str]]] = defaultdict(set)
    for res1_ID, res2_ID, PDB_ID in zip(residue_pair_df.residue_1.values, residue_pair_df.residue_2.values, residue_pair_df.PDB_ID.values):
        res1_full_ID: str = res1_ID + res1_resname # Ex: 'A1G', that is residue A1 which is a Glycine
        res2_full_ID: str = res2_ID + res2_resname
        pair_of_full_residue_IDs: Tuple[str,str] = get_sorted_2_tuple((res1_full_ID, res2_full_ID)) # Sorting is needed to be able to then find PDBs with the residue pair in the correct 3 geometric descriptors later
        
        PDBs_that_contain_the_residue_pair[PDB_ID].add(pair_of_full_residue_IDs)

    return PDBs_that_contain_the_residue_pair

def get_PDBs_with_residue_pair_in_the_correct_3_geometric_descriptors(
        PDBs_with_residue_pair_with_correct_C_alpha_distance: Dict[str, Set[Tuple[str,str]]], 
        PDBs_with_residue_pair_with_correct_sidechain_CMR_distance: Dict[str, Set[Tuple[str,str]]], 
        PDBs_with_residue_pair_with_correct_vector_angle: Dict[str, Set[Tuple[str,str]]]
    ) -> Dict[str, Set[Tuple[str,str]]]:
    """
    """
    # First determine the subset of PDBs that have 1 or more residue pair(s) in the 3 geometric descriptors, even if they are different pairs.
    PDBs_with_residue_pair_in_the_correct_3_geometric_descriptors = set.intersection(
        set(PDBs_with_residue_pair_with_correct_C_alpha_distance.keys()),
        set(PDBs_with_residue_pair_with_correct_sidechain_CMR_distance.keys()),
        set(PDBs_with_residue_pair_with_correct_vector_angle.keys())
    )

    # Then determine the PDBs that have at least one residue pair that corresponds to all 3 geometric descriptors at the same time.
    PDBs_that_contain_the_residue_pair: Dict[str, Set[Tuple[str,str]]] = {}
    for PDB_ID in PDBs_with_residue_pair_in_the_correct_3_geometric_descriptors:
        residue_pairs_in_correct_3_geometric_descriptors: Set[Tuple[str,str]] = set.intersection(
            PDBs_with_residue_pair_with_correct_C_alpha_distance[PDB_ID],
            PDBs_with_residue_pair_with_correct_sidechain_CMR_distance[PDB_ID],
            PDBs_with_residue_pair_with_correct_vector_angle[PDB_ID]
        )
        if residue_pairs_in_correct_3_geometric_descriptors:
            PDBs_that_contain_the_residue_pair[PDB_ID] = residue_pairs_in_correct_3_geometric_descriptors

    return PDBs_that_contain_the_residue_pair

def get_PDBs_that_contain_the_residue_pair(
        pair_of_full_residue_IDs: Tuple[str,str], residue_pair_data: Residue_pair_data, distance_delta_thr: float, angle_delta_thr: float, 
        index_folder_path: Path, compression: str
    ) -> Dict[str, Set[Tuple[str,str]]]:
    """
    ...
    """
    res1_full_ID, res2_full_ID = pair_of_full_residue_IDs
    res1_resname, res2_resname = res1_full_ID[-1], res2_full_ID[-1]
    pair_of_residues = sort_and_join_2_strings(res1_resname, res2_resname) # The index only contains lexycographically sorted reside pairs (ex: GA doesn't exist, only AG)

    # Find PDBs that contain the residue pair in each of the 3 geometric descriptors
    PDBs_with_residue_pair_with_correct_C_alpha_distance = search_index_for_PDBs_that_contain_the_residue_pair(
        pair_of_residues=pair_of_residues, 
        geometric_descriptor_index_folder=index_folder_path / 'C_alpha_distance',
        value_range=(residue_pair_data.C_alpha_distance - distance_delta_thr, residue_pair_data.C_alpha_distance + distance_delta_thr),
        compression=compression,
    )
    PDBs_with_residue_pair_with_correct_sidechain_CMR_distance = search_index_for_PDBs_that_contain_the_residue_pair(
        pair_of_residues=pair_of_residues, 
        geometric_descriptor_index_folder=index_folder_path / 'sidechain_CMR_distance',
        value_range=(residue_pair_data.sidechain_CMR_distance - distance_delta_thr, residue_pair_data.sidechain_CMR_distance + distance_delta_thr),
        compression=compression,
    )
    PDBs_with_residue_pair_with_correct_vector_angle = search_index_for_PDBs_that_contain_the_residue_pair(
        pair_of_residues=pair_of_residues,
        geometric_descriptor_index_folder=index_folder_path / 'vector_angle',
        value_range=(residue_pair_data.vector_angle - angle_delta_thr, residue_pair_data.vector_angle + angle_delta_thr),
        compression=compression,
    )

    PDBs_that_contain_the_residue_pair = get_PDBs_with_residue_pair_in_the_correct_3_geometric_descriptors(
        PDBs_with_residue_pair_with_correct_C_alpha_distance, 
        PDBs_with_residue_pair_with_correct_sidechain_CMR_distance, 
        PDBs_with_residue_pair_with_correct_vector_angle
    )

    return PDBs_that_contain_the_residue_pair

residue_pair_to_PDB_map_type_alias: TypeAlias = Dict[Tuple[str,str], Dict[str, Set[Tuple[str,str]]]] # For mypy annotation
def get_residue_pair_to_PDB_map(
        all_pairs_of_residues_to_check: Dict[Tuple[str,str], Residue_pair_data], distance_delta_thr: float, angle_delta_thr: float, index_folder_path: Path, 
        compression: str, concurrent_executor: ProcessPoolExecutor
    ) -> residue_pair_to_PDB_map_type_alias:
    """
    ...
    """
    residue_pair_to_PDB_map: residue_pair_to_PDB_map_type_alias = {}

    submitted_futures: Dict[Future[Dict[str, Set[Tuple[str,str]]]], Tuple[str,str]] = {
        concurrent_executor.submit(get_PDBs_that_contain_the_residue_pair, pair_of_full_residue_IDs, residue_pair_data, distance_delta_thr, angle_delta_thr, index_folder_path, compression):pair_of_full_residue_IDs
        for pair_of_full_residue_IDs, residue_pair_data in all_pairs_of_residues_to_check.items()
    }

    for future in as_completed(submitted_futures):
        if future.exception():
            raise future.exception() # type: ignore

        pair_of_full_residue_IDs = submitted_futures[future] 
        PDBs_that_contain_the_residue_pair = future.result()
        
        residue_pair_to_PDB_map[pair_of_full_residue_IDs] = PDBs_that_contain_the_residue_pair

    return residue_pair_to_PDB_map

def update_map_of_PDBs_with_all_residue_pairs(
        map_of_PDBs_with_all_residue_pairs: Dict[str, Set[Tuple[str,str]]], new_residue_pair_data: Dict[str, Set[Tuple[str,str]]]
    ) -> Dict[str, Set[Tuple[str,str]]]:
    """
    ...
    """
    updated_set_of_PDBs_with_all_residue_pairs = set.intersection(
        set(map_of_PDBs_with_all_residue_pairs), 
        set(new_residue_pair_data)
    )
    
    for PDB_ID in list(map_of_PDBs_with_all_residue_pairs.keys()):
        if PDB_ID not in updated_set_of_PDBs_with_all_residue_pairs:
            del map_of_PDBs_with_all_residue_pairs[PDB_ID] # We remove PDBs that no longer have all the residue pairs
        else:
            map_of_PDBs_with_all_residue_pairs[PDB_ID].update(new_residue_pair_data[PDB_ID]) # We update the set of residue pairs of the PDB

    return map_of_PDBs_with_all_residue_pairs

def find_PDBs_with_all_residue_pairs(
        all_motifs_MST: List[nx.Graph], residue_pair_to_PDB_map: residue_pair_to_PDB_map_type_alias
    ) -> Dict[nx.Graph, Dict[str, Set[Tuple[str,str]]]]:
    """
    """
    # The algorithm determines which PDBs contain all the residue pairs of a given motif MST by simply iterating over each residue pair 
    # and calculating the intersection between the current map of PDBs with all residue pairs and the PDBs that contain
    # the given residue pair that is being checked.
    PDBs_with_all_residue_pairs: Dict[nx.Graph, Dict[str, Set[Tuple[str, str]]]] = {}
    for motif_MST in all_motifs_MST:
        pairs_of_residues_to_check: List[Tuple[str,str]] = list(motif_MST.edges)
        pairs_of_residues_to_check = [get_sorted_2_tuple(pair_of_full_residue_IDs) for pair_of_full_residue_IDs in pairs_of_residues_to_check]
        
        # map_of_PDBs_with_all_residue_pairs must be initialized with the PDBs of a residue pair in order to be able to do the iterative intersection,
        # otherwise we would always get an empty set because of the initially empty map_of_PDBs_with_all_residue_pairs.
        initial_pair_of_full_residue_IDs = pairs_of_residues_to_check.pop()
        map_of_PDBs_with_all_residue_pairs: Dict[str, Set[Tuple[str,str]]] = defaultdict(set, residue_pair_to_PDB_map[initial_pair_of_full_residue_IDs])

        for pair_of_full_residue_IDs in pairs_of_residues_to_check:
            map_of_PDBs_with_all_residue_pairs = update_map_of_PDBs_with_all_residue_pairs(
                map_of_PDBs_with_all_residue_pairs, 
                residue_pair_to_PDB_map[pair_of_full_residue_IDs]
            )


        if map_of_PDBs_with_all_residue_pairs:
            PDBs_with_all_residue_pairs[motif_MST] = map_of_PDBs_with_all_residue_pairs

    return PDBs_with_all_residue_pairs

def add_resname_as_node_attribute(graph: nx.Graph) -> None:
    """
    """
    nx.set_node_attributes(graph, {node:{'resname':node[-1]} for node in graph.nodes}) # Each node is a residue_full_ID so [-1] returns the residue (ex: 'G', for Glycine)
    return

def run_subgraph_monomorphism(motif_MST: nx.Graph, pairs_of_residues: Set[Tuple[str, str]]) -> List[nx.Graph]:
    """
    The returned list can be empty.
    """
    candidate_PDB_graph = nx.Graph(pairs_of_residues)
    add_resname_as_node_attribute(candidate_PDB_graph)

    graph_matcher = nx.algorithms.isomorphism.GraphMatcher(
        G1 = candidate_PDB_graph, G2 = motif_MST, 
        node_match = lambda node1,node2: node1['resname'] == node2['resname'] # Match based on residue name
    )

    monomorphism_checked_motifs: List[nx.Graph] = [] # Each PDB can have multiple motifs (ie: homodimers) -> List[nx.Graph]
    residue_mapping_dict: Dict[str,str]
    for residue_mapping_dict in graph_matcher.subgraph_monomorphisms_iter():
        residues_of_the_similar_motif = list(residue_mapping_dict.keys())
        similar_motif_graph: nx.Graph = candidate_PDB_graph.subgraph(residues_of_the_similar_motif).copy()
        
        setattr(similar_motif_graph, 'residue_mapping_dict', residue_mapping_dict) # Used for RMSD calculation

        monomorphism_checked_motifs.append(similar_motif_graph)

    return monomorphism_checked_motifs

def filter_out_PDBs_with_unconnected_residue_pairs(
        PDBs_with_all_residue_pairs: Dict[nx.Graph, Dict[str, Set[Tuple[str, str]]]], concurrent_executor: ProcessPoolExecutor
    ) -> Dict[nx.Graph, Dict[str, List[nx.Graph]]]:
    """
    """
    # To know if a PDB contains a set of connected residue pairs forming a similar motif, we use subgraph monomorphism to perform a matching between a reference 
    # motif's graph and the graph generated from all the selected residue pairs of a candidate PDB structure. The monomorphism is done based on the residue names,
    # which have to be identical between the two graphs. Note that we use subgraph monomorphism instead of simple graph monomorphism because PDBs might have more 
    # than 1 similar motif, for example a motif might be present twice in a homodimer, so we need to check all possible subgraphs in the graph generated from the selected residue pairs.
    # Also note that isomorphism cannot be used as it imposes an exact match of both the nodes and edges between all the nodes, which results in certain False Negatives
    # given the edges simply correspond to the presence of a pair of residues, they are not chemical bonds. For example, sub-graph isomorphism fails to find a match for residues 31-38 in
    # PDB AF-G5EB01-F1-model_v4 despite the PDB being in the index. Indeed, when using a distance threshold > 1.5 and an angle threshold > 10°, this leads to 
    # the occurence of an additional AE edge between residue A32A and A35E, and that edge causes isomorphism to fail, unlike monomorphism which correctly finds the PDB.
    for motif_MST in PDBs_with_all_residue_pairs.keys():
        add_resname_as_node_attribute(motif_MST) # Needed for subgraph monomorphism, see below.

    # In order to be able to take full advantage of parallelisation (even when there is only 1 motif_MST to solve !) we have to parallelize
    # the subgraph monomorphism check of each PDB, rather than parallelize each motif_MST.
    submited_futures: Dict[Future[List[nx.Graph]], Tuple[nx.Graph, str]] = {}
    for motif_MST, map_of_candidate_PDBs_and_their_residue_pairs in PDBs_with_all_residue_pairs.items():
        for PDB_ID, pairs_of_residues in map_of_candidate_PDBs_and_their_residue_pairs.items():
            future = concurrent_executor.submit(run_subgraph_monomorphism, motif_MST, pairs_of_residues)
            submited_futures[future] = (motif_MST, PDB_ID)

    filtered_PDBs_with_all_residue_pairs: Dict[nx.Graph, Dict[str, List[nx.Graph]]] = defaultdict(dict)
    for future in as_completed(submited_futures):
        if future.exception():
            raise future.exception() # type: ignore

        motif_MST, PDB_ID = submited_futures[future] 
        monomorphism_checked_motifs = future.result()

        if monomorphism_checked_motifs: # List can be empty
            filtered_PDBs_with_all_residue_pairs[motif_MST][PDB_ID] = monomorphism_checked_motifs

    return filtered_PDBs_with_all_residue_pairs

def get_PDBs_with_similar_motifs(
        motif_MST: nx.Graph, motif_residues_data: Dict[str, Residue], index_folder_path: Path, max_n_mutated_residues: int, 
        residue_type_policy: Union[str, Dict[str,List[str]]], distance_delta_thr: float, angle_delta_thr: float, compression: str, n_cores: int
    ) -> Dict[nx.Graph, Dict[str, List[nx.Graph]]]:
    """
    ...
    """
    # This algorithm has 3 steps:
    # - First determine the PDBs that contain each residue pair (i.e generate residue_pair_to_PDB_map)
    # - Then get the PDBs that contain all the residue pairs in each given motif (remember that users can generate mutated motifs, so there could be > 1 motif. See get_all_motif_MSTs_generator)
    # - Finally filter the list of candidate PDBs to only keep those where the residue pairs are connected
    
    # The most computationally intensive part of the code is the actual loading of the data for all the residue pairs and to 
    # then find the PDBs that contain the residue pair. Therefore, we first determine the PDBs that contain each residue pair 
    # present in all the available motif MSTs, and then use that to determine the PDBs that contain a similar motif for each respective motif MST.
    # Although we could in theory parallelize each motif MST instead, that would require sharing the residue_pair_to_PDB_map between the processes,
    # which would add overhead and complexify the code.
    all_motifs_MST = list(get_all_motif_MSTs_generator(motif_MST, max_n_mutated_residues, residue_type_policy, motif_residues_data))
    all_pairs_of_residues_to_check = get_all_pairs_of_residues_to_check(all_motifs_MST)

    with ProcessPoolExecutor(n_cores) as concurrent_executor:
        residue_pair_to_PDB_map = get_residue_pair_to_PDB_map(all_pairs_of_residues_to_check, distance_delta_thr, angle_delta_thr, index_folder_path, compression, concurrent_executor)

        # Its not worth parallelizing find_PDBs_with_all_residue_pairs as its actually quite fast and the added overhead of parallelizing + having to transfer the results back to the main thread isn't worth it.
        PDBs_with_all_residue_pairs = find_PDBs_with_all_residue_pairs(all_motifs_MST, residue_pair_to_PDB_map)

        # After finding PDBs that contain all the residue pairs in their correct geometric arrangement, we need to make sure 
        # these pairs are connected and not just scattered. PDBs with connected pairs correspond to those that contain a similar motif(s). 
        # Connected pairs example: [('A1P', 'A4C'), ('A4C', 'A9L'), ('A9L', 'A10K')]
        # Unconnected pairs example: [('A1P', 'A4C'), ('A54C', 'A60L'), ('A19L', 'A22K')]
        filtered_PDBs_with_all_residue_pairs = filter_out_PDBs_with_unconnected_residue_pairs(PDBs_with_all_residue_pairs, concurrent_executor)

    return filtered_PDBs_with_all_residue_pairs

def search_index_for_PDBs_with_similar_motifs(
        index_folder_path: Path, PDB_file: Path, motif: Tuple[str,...], residue_type_policy: Union[str, Dict[str,List[str]]], max_n_mutated_residues: int, 
        distance_delta_thr: float, angle_delta_thr: float, n_cores: int
    ) -> Tuple[nx.Graph, Dict[nx.Graph, Dict[str, List[nx.Graph]]]]:
    """
    ...
    """
    if not index_folder_exists(index_folder_path):
        raise ValueError("Could not find all the index folders and files. Did you previously create the index with the 'create-index' command ?")
    
    motif_residues_data = extract_motif_residues_from_PDB_file(PDB_file, motif)
    data_of_all_pairs_of_residues_in_motif = get_data_of_all_pairs_of_residues_in_motif(motif_residues_data)
    # It would be inefficient to search the index for every single pair of residues in the motif in order to find PDBs that have a similar 
    # motif. Instead we can determine the Minimum Spanning Tree (MST) of the motif to limit the search to a subset of pairs that covers all the residues.
    motif_MST = get_minimum_spanning_tree(data_of_all_pairs_of_residues_in_motif)

    compression = detect_the_compression_algorithm_used_in_the_index(index_folder_path)
    PDBs_with_similar_motifs = get_PDBs_with_similar_motifs(
        motif_MST, 
        motif_residues_data, 
        index_folder_path,
        max_n_mutated_residues, 
        residue_type_policy, 
        distance_delta_thr, 
        angle_delta_thr,
        compression,
        n_cores
    )

    return motif_MST, PDBs_with_similar_motifs
