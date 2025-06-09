from pathlib import Path
import os

def get_files_info(working_directory, directory=None):
    working_directory = Path(working_directory).expanduser().resolve()
    if directory is None:
        directory = working_directory
    else:
        directory = Path(directory)
        if not directory.is_absolute():
            # Interpret as relative to the working_directory
            directory = (working_directory / directory).resolve()
        else:
            # Resolve absolute path directly
            directory = directory.resolve()

    # Check that both paths are directories
    if not working_directory.is_dir():
        return(f'Error: "{working_directory}" is not a directory')
        

    if not directory.is_dir():
        return(f'Error: "{directory}" is not a directory')
        

    try:
        directory.relative_to(working_directory)
    except ValueError:
        return(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        
    
    # print(os.listdir(working_directory))
    # files = os.listdir(working_directory)
    file_dict = {}
    for file in os.listdir(directory):
        path_str = os.path.join(directory, file)
        is_dir = os.path.isdir(path_str)
        file_size = os.path.getsize(path_str) if not is_dir else os.path.getsize(path_str)  # Optionally omit size for dirs

        file_dict[file] = {
            "file_size": file_size,
            "is_dir": is_dir
        }
    
    files_string = ""
    print("\n")
    for key in list(file_dict.keys()):
        #print(key)
        files_string += (f"- {key}: file_size={file_dict[key]["file_size"]} bytes, is_dir={file_dict[key]["is_dir"]}\n")
    return files_string