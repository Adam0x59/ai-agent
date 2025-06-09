import os
from functions.check_path_inputs import *
from config import MAX_CHARS

def get_file_content(working_directory, file_path):

    file_status = check_path_inputs(working_directory, file_path)

    if not file_status["path_to_check_rel"]:
        return(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
    
    if file_status["path_data"]["dir"]:
        return(f'Error: File not found or is not a regular file: "{file_path}"')
    
    try:
        with open(file_status["path_to_check"], "r") as f:
            file_contents = f.read()
    except Exception as e:
        return f'Error: {str(e)}'

    if len(file_contents) > MAX_CHARS:
        file_contents = file_contents[:MAX_CHARS]
        file_contents = file_contents + f'[...File "{file_path}" truncated at 10000 characters]'

    return file_contents

    pass