import os
from pathlib import Path

def check_path_inputs(working_directory, path_to_check):
    path_is_working_dir = False

    if working_directory is None:
        return f"Error: working_directory - {working_directory} is empty!"
    working_directory = Path(working_directory).expanduser().resolve()
    
    wd_absolute = working_directory.is_absolute()

    if path_to_check is None:
        path_to_check = working_directory
        path_is_working_dir = True
    
    path_to_check = Path(path_to_check)
    path_absolute = path_to_check.is_absolute()
    
    if not path_absolute:
        path_to_check = (working_directory / path_to_check).resolve()
    path_to_check = path_to_check.resolve()

    path_dir = path_to_check.is_dir()
    wd_dir = working_directory.is_dir()

    try:
        path_to_check.relative_to(working_directory)
        path_to_check_rel = True
    except ValueError:
        path_to_check_rel = False

    return {
            "working_dir": working_directory, "wd_data":{ "dir": wd_dir, "absolute": wd_absolute}, 
            "path_to_check": path_to_check, "path_data":{ "dir": path_dir , "absolute": path_absolute, "path_is_working_dir": path_is_working_dir}, 
            "path_to_check_rel": path_to_check_rel, 
                }