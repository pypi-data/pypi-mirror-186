""" Some helpful file and folder functions
Copyright Nanosurf AG 2021
License - MIT
"""
import os
import pathlib
from datetime import datetime

def create_filename_with_timestamp(base_name: str, extension: str = '.dat', separator: str = "_") -> str:
    """Make filename"""
    current_datetime = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = base_name + separator + current_datetime + extension
    return filename

def create_folder(file_path: pathlib.Path) -> bool:
    """ Make sure the folder exists. 
    If needed, it  creates the intermediate directories starting from root.
    """
    done = False
    try:
        if not file_path.is_dir():
            os.makedirs(file_path, exist_ok=True)
        done = file_path.is_dir()
    except:
        pass
    return done

def create_unique_folder(base_name: str, folder: pathlib.Path, add_timestamp: bool = True, separator: str = '_') -> pathlib.Path:
    """Create a unique folder.  The folder name has the structure of 'base_name_timestamp_index'
    The timestamp is optional, set argument add_timestamp=False to suppress it.
    A index is added, if the base_name folder (with optional timestamp) is not unique already. 
    The index starts at zero and is incremented until a unique name is found.

    Parameter
    ---------
    base_name: str
        The new folder name has the structure of 'base_name_timestamp_index'
    folder: pathlib.Path
        The folder in which the new subfolder with the unique name shall be created
    add_timestamp: bool, optional, defaults to True
        If set to True, a timestamp in the format of %Y%m%d-%H%M%S is added
    separator : str, optional, defaults to '_'
        The separation character use to separate parts of the folder name. 

    Result
    ------
        filepath: pathlib.Path
            path object to newly created folder. If creation was not successful the return value is None
    """
    if add_timestamp:
        base_name = create_filename_with_timestamp(base_name, extension="", separator=separator)

    done = create_folder(folder)
    if done:
        data_folder_name = base_name
        filepath = pathlib.Path(folder) / pathlib.Path(data_folder_name)
        i = 0
        while filepath.is_dir():
            data_folder_name = f"{base_name}_{i:03d}"
            filepath = pathlib.Path(folder) / pathlib.Path(data_folder_name)
            i += 1
        done = create_folder(filepath)
    if not done:
        filepath = None
    return filepath

