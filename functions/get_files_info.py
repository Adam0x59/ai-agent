import os
from functions.check_path_inputs import *

def get_files_info(working_directory, directory=None):
    file_status = check_path_inputs(working_directory, directory)
    
    working_directory = file_status["working_dir"]
    directory = file_status["path_to_check"]

    if not file_status["wd_data"]["dir"]:
        return(f'Error: "{working_directory}" is not a directory')
    if not file_status["path_data"]["dir"]:
        return(f'Error: "{directory} is not a directory')
    if not file_status["path_to_check_rel"]:
        return(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    
    file_dict = {}
    for file in os.listdir(directory):
        path_str = os.path.join(directory, file)
        is_dir = os.path.isdir(path_str)
        file_size = os.path.getsize(path_str) if not is_dir else os.path.getsize(path_str)

        file_dict[file] = {"file_size": file_size, "is_dir": is_dir}
    
    files_string = ""
    print("\n")
    for key in list(file_dict.keys()):
        files_string += (f"- {key}: file_size={file_dict[key]["file_size"]} bytes, is_dir={file_dict[key]["is_dir"]}\n")
    return files_string