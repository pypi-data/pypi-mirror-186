import concurrent.futures
from concurrent.futures import ProcessPoolExecutor
from itertools import groupby
from pathlib import Path
from typing import Dict, Iterator, List, Set, Tuple

import pandas as pd
from typing_extensions import TypeAlias

from pydiscomotif.constants import (INDEX_ANGLE_BIN_SIZE,
                                    INDEX_DISTANCE_BIN_SIZE,
                                    INDEX_MAX_DISTANCE_VALUE)
from pydiscomotif.data_containers import Residue
from pydiscomotif.index_folders_and_files import create_index_folder_tree
from pydiscomotif.residue_data_dicts import \
    generate_compressed_residue_data_from_PDB_file
from pydiscomotif.utils import (
    angle_between_two_vectors,
    detect_the_compression_algorithm_used_in_the_index,
    generate_all_geometric_descriptors_and_pairs_of_residues_combinations,
    get_bin_number, get_PDB_ID_from_file_path, pairwise_euclidean_distance,
    pickle_and_compress_python_object, read_compressed_and_pickled_file)


def get_geometric_attribute(geometric_descriptor: str) -> str:
    return geometric_descriptor.rsplit('_', maxsplit=1)[0] # Ex: C_alpha_distance -> C_alpha

def get_residue_specific_data(residue_data: Dict[str, Residue], residue_name: str) -> Dict[str, Residue]:
    """
    ...
    """
    return {residue_ID:residue for residue_ID, residue in residue_data.items() if residue.resname == residue_name}

index_data_type_alias: TypeAlias = List[Tuple[float, str, str, str]] # For mypy annotation
def get_euclidean_distance_index_data(
        residue_data_of_residue_1: Dict[str, Residue], residue_data_of_residue_2: Dict[str, Residue], geometric_attribute:str , PDB_ID: str
    ) -> index_data_type_alias:
    """
    """
    index_data: index_data_type_alias = []
    for residue_1_ID, residue_1 in residue_data_of_residue_1.items():
        residue_1_geometric_descriptor = residue_1[geometric_attribute]
        for residue_2_ID, residue_2 in residue_data_of_residue_2.items():
            if residue_1_ID == residue_2_ID: # In the case of identical pairs of residues (ex: AA, GG, ...), we don't want to store the distance of the residue with itself.
                continue

            residue_2_geometric_descriptor = residue_2[geometric_attribute]

            distance = pairwise_euclidean_distance(residue_1_geometric_descriptor, residue_2_geometric_descriptor)
            distance = float(distance)

            if distance <= INDEX_MAX_DISTANCE_VALUE:
                index_data.append((round(distance, 2), residue_1_ID, residue_2_ID, PDB_ID))

    return index_data

def get_angle_index_data(
        residue_data_of_residue_1: Dict[str, Residue], residue_data_of_residue_2: Dict[str, Residue], geometric_attribute:str , PDB_ID: str
    ) -> index_data_type_alias:
    """
    """
    # Use the C alpha index data do determine which pairs of residues to add in the angle index data.
    C_alpha_index_data = get_euclidean_distance_index_data(residue_data_of_residue_1, residue_data_of_residue_2, 'C_alpha', PDB_ID)
    pairs_of_residues_within_distance_thr: Set[Tuple[str, str]] = {
        (residue_1_ID, residue_2_ID)
        for _, residue_1_ID, residue_2_ID, _ in C_alpha_index_data
    }
    del C_alpha_index_data

    index_data: index_data_type_alias = []
    for residue_1_ID, residue_1 in residue_data_of_residue_1.items():
        residue_1_geometric_descriptor = residue_1[geometric_attribute]
        for residue_2_ID, residue_2 in residue_data_of_residue_2.items():
            if (residue_1_ID, residue_2_ID) not in pairs_of_residues_within_distance_thr:
                continue
                
            residue_2_geometric_descriptor = residue_2[geometric_attribute]
            
            angle = angle_between_two_vectors(residue_1_geometric_descriptor, residue_2_geometric_descriptor)
            angle = float(angle)

            index_data.append((round(angle, 2), residue_1_ID, residue_2_ID, PDB_ID))

    return index_data

def generate_index_data(residue_data: Dict[str, Residue], PDB_ID:str,  geometric_descriptor: str, pair_of_residues: str) -> index_data_type_alias:
    """
    ...
    """
    residue_1_name, residue_2_name = pair_of_residues[0], pair_of_residues[1]
    geometric_attribute = get_geometric_attribute(geometric_descriptor) # Ex: C_alpha
    
    residue_data_of_residue_1 = get_residue_specific_data(residue_data, residue_1_name)
    residue_data_of_residue_2 = get_residue_specific_data(residue_data, residue_2_name)

    if geometric_descriptor == 'vector_angle':
        index_data = get_angle_index_data(residue_data_of_residue_1, residue_data_of_residue_2, geometric_attribute, PDB_ID)
    else:
        index_data = get_euclidean_distance_index_data(residue_data_of_residue_1, residue_data_of_residue_2, geometric_attribute, PDB_ID)

    return index_data

def write_index_data_to_corresponding_bin_files(
        cumulated_index_data: List[Tuple[float, str, str, str]], pair_of_residues: str, geometric_descriptor_folder: Path, geometric_descriptor: str
    ) -> None:
    """
    ...
    """
    # The bin files contain data of half open interals, ie [0.0, 0.5), [0.5, 1.0), ... for distances. The bin is determined by simply calculating
    # the floor division between the metric value and the bin size. Note that it's the use of floor division that leads to half open intervals.
    # Distance bin example: value = 2.3 -> 2.3 // 0.5 = 4 = bin number
    # Angle bin example   : value = 150 -> 150 // 10 = 15 = bin number
    # To avoid opening and closing a file for each row, we group the rows by their associated bin to open and close 
    # the corresponding file only once.
    bin_size = INDEX_ANGLE_BIN_SIZE if geometric_descriptor == 'vector_angle' else INDEX_DISTANCE_BIN_SIZE

    sorted_cumulated_index_data = sorted(cumulated_index_data, key=lambda tuple_:tuple_[0])
    grouped_cumulated_index_data = groupby(sorted_cumulated_index_data, key=lambda tuple_:get_bin_number(tuple_[0], bin_size))
    for bin_number, bin_index_data in grouped_cumulated_index_data:
        
        with open(geometric_descriptor_folder / f'{pair_of_residues}_{bin_number}.csv', 'a') as file_handle:
            for row in bin_index_data:
                file_handle.write(','.join((str(element) for element in row)) + '\n')

    return

def create_index_files_of_geometric_descriptor_and_pair_of_residues_combination(
        geometric_descriptor_and_pair_of_residues_combination: Tuple[str, str], PDB_files_to_index: List[Path], 
        index_folder_path: Path, compression: str
    ) -> None:
    """
    ...
    """
    geometric_descriptor, pair_of_residues = geometric_descriptor_and_pair_of_residues_combination # NOTE: The pair of residues is guaranteed to be lexicographically sorted (ei AG or CP, it will never be GA or PC). See generate_all_geometric_descriptors_and_pairs_of_residues_combinations
    compressed_residue_data_folder = index_folder_path / 'residue_data_folder'
    geometric_descriptor_folder = index_folder_path / geometric_descriptor

    cumulated_index_data: index_data_type_alias = []
    for PDB_file in PDB_files_to_index:
        PDB_ID = get_PDB_ID_from_file_path(PDB_file)
        compressed_residue_data_file_path = compressed_residue_data_folder / f'{PDB_ID}.{compression}' 
        residue_data: Dict[str,Residue] = read_compressed_and_pickled_file(compressed_residue_data_file_path)
        
        index_data = generate_index_data(residue_data, PDB_ID, geometric_descriptor, pair_of_residues)

        cumulated_index_data.extend(index_data)
        
        # To limit RAM usage even when dealing with hundreds of thousands of PDB files, the index data is periodically written
        # to a csv file on disk.
        if len(cumulated_index_data) >= 1000:
            write_index_data_to_corresponding_bin_files(cumulated_index_data, pair_of_residues, geometric_descriptor_folder, geometric_descriptor)
            cumulated_index_data.clear()

    # The above condition never triggers for the last chunk of data, so we need to call the functions one last time.
    write_index_data_to_corresponding_bin_files(cumulated_index_data, pair_of_residues, geometric_descriptor_folder, geometric_descriptor)
    cumulated_index_data.clear()

    # Replace each csv file with a pickled and compressed pandas dataframe. If the pickled and compressed file already
    # exists that means we are in update mode, so we simply read the file and concatenate the dataframes.
    for binned_data_csv_file_path in geometric_descriptor_folder.glob(f'{pair_of_residues}_*.csv'):
        bin_index_data_df = pd.read_csv(
            binned_data_csv_file_path, 
            names=['geometric_value', 'residue_1','residue_2','PDB_ID'], 
            index_col='geometric_value',
        )
        output_file_path=binned_data_csv_file_path.with_suffix(f'.{compression}') # Ex: /home/user_name/database_folder/pyDiscoMotif_index/C_alpha_distance/AG_4.bz2
        if output_file_path.exists(): 
            # Update mode
            bin_index_data_df = pd.concat((bin_index_data_df, read_compressed_and_pickled_file(output_file_path)), axis=0, copy=False) 
        
        # We sort the data so that we can use binary search later when doing motif search
        bin_index_data_df.sort_index(inplace=True) 

        # Replace the csv file with the pickled and compressed pandas dataframe
        binned_data_csv_file_path.unlink()
        pickle_and_compress_python_object(
            python_object=bin_index_data_df,
            output_file_path=output_file_path
        )

    return

def update_file_of_indexed_PDB_files(index_folder: Path, new_PDB_IDs: Iterator[str]) -> None:
    """
    ...
    """
    with open(index_folder / 'indexed_PDB_files.txt', 'a') as file_handle:
        for PDB_ID in new_PDB_IDs:
            file_handle.write(PDB_ID + '\n')
    return

def index_PDB_files(PDB_files_to_index: List[Path], index_folder_path: Path, compression: str, n_cores: int) -> None:
    """
    """
    with ProcessPoolExecutor(max_workers=n_cores) as executor:
        # We first parse all the PDB files to extract and format the residue data of interest (residue name, C alpha coordinates, etc), 
        # which is then saved as a pickle and compressed file. This is done to avoid parsing anew each PDB file 630 times, instead 
        # we just load these files which contains a simple python dictionary, which is ~15x faster.
        submited_futures = [executor.submit(generate_compressed_residue_data_from_PDB_file, PDB_file_path, index_folder_path, compression) for PDB_file_path in PDB_files_to_index]
        for future in concurrent.futures.as_completed(submited_futures):
            if future.exception():
                raise future.exception() # type: ignore 
        
        # Each worker processes 1 of the 630 geometric descriptor + residue pair combinations. 
        # The output is a series of pickled and compressed files for each combination that each contain the data of a bin 
        # e.g .../pyDiscoMotif_index/C_alpha_distance/AG_4.bz2 contains the occurences of all pairs of AG with a C alpha distance that is between 2 and 2.5 angstrooms.
        all_geometric_descriptors_and_pairs_of_residues_combinations = generate_all_geometric_descriptors_and_pairs_of_residues_combinations()
        submited_futures = [executor.submit(create_index_files_of_geometric_descriptor_and_pair_of_residues_combination, combination, PDB_files_to_index, index_folder_path, compression) for combination in all_geometric_descriptors_and_pairs_of_residues_combinations]
        for future in concurrent.futures.as_completed(submited_futures):
            if future.exception():
                raise future.exception() # type: ignore


    # To allow users to update the index with new structures we need to keep track of the PDB files that have already been indexed.
    update_file_of_indexed_PDB_files(
        index_folder_path, 
        new_PDB_IDs = (get_PDB_ID_from_file_path(PDB_file_path) for PDB_file_path in PDB_files_to_index)
    )
    
    return

def create_index_folder(database_path: Path, pattern: str, index_folder_path: Path, compression: str, n_cores: int) -> None:
    """Indexes all the pairs of residues in the PDB files of the given database. PDB files compressed as .gz are accepted."""
    PDB_files_to_index: List[Path] = list(database_path.rglob(pattern)) # rglob = recursively glob through the directory and subdirectory
    if not PDB_files_to_index:
        raise ValueError(f"No files were found that match the pattern {pattern}.")
    
    create_index_folder_tree(index_folder_path)

    index_PDB_files(PDB_files_to_index, index_folder_path, compression, n_cores)
    return

def get_set_of_already_indexed_PDBs(index_folder_path: Path) -> Set[str]:
    """
    Returns the set of PDBs that have already been added to the index.
    """
    with open(index_folder_path / 'indexed_PDB_files.txt', 'rt') as file_handle:
        set_of_already_indexed_PDBs = set(PDB_ID.strip() for PDB_ID in file_handle.readlines())

    return set_of_already_indexed_PDBs

def update_index_folder(database_path: Path, pattern: str, index_folder_path: Path, n_cores: int) -> None:
    """Updates an existing index with new PDB files."""
    set_of_already_indexed_PDBs = get_set_of_already_indexed_PDBs(index_folder_path)
    PDB_files_to_index: List[Path] = []
    for PDB_file in database_path.rglob(pattern):
        PDB_ID = get_PDB_ID_from_file_path(PDB_file)
        if PDB_ID not in set_of_already_indexed_PDBs:
            PDB_files_to_index.append(PDB_file)
    del set_of_already_indexed_PDBs # No longer needed
    
    if not PDB_files_to_index:
        raise ValueError(f"No new files were found that match the pattern {pattern}.")

    compression = detect_the_compression_algorithm_used_in_the_index(index_folder_path)

    index_PDB_files(PDB_files_to_index, index_folder_path, compression, n_cores)

    print(f'{len(PDB_files_to_index)} new structures have been added to the index.')
    return
