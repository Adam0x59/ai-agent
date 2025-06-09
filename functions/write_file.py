import os
from functions.check_path_inputs import *

def write_file(working_directory, file_path, content):
    
    file_status = check_path_inputs(working_directory, file_path)

    if not file_status["path_to_check_rel"]:
        return(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')

    if not file_status["path_data"]["dir_path"]:
        try:
            print(file_status["path_to_check"])
            os.makedirs(file_status["path_data"]["dir_path"])
        except Exception as e:
            return f'Error: {str(e)}'

    try:
        with open(file_status["path_to_check"], "w") as f:
            f.write(content)
    except Exception as e:
        return f'Error: {str(e)}'
    
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
