import subprocess
from string import *
from functions.check_path_inputs import *

def run_python_file(working_directory, file_path):
    
    file_status = check_path_inputs(working_directory, file_path)

    if not file_status["path_to_check_rel"]:
        return(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')    
    
    if not file_status["path_data"]["file_exists"]:
        return(f'Error: File "{file_path}" not found.')
    
    if not str(file_status["path_to_check"]).endswith(".py"):
        return(f'Error: "{file_path}" is not a Python file.')
    
    try:
        result = subprocess.run(
            f'python3 ./{file_path}', 
            shell=True, 
            timeout=30, 
            capture_output=True, 
            cwd=file_status["working_dir"]
        )
    except Exception as e:
        return f'Error: executing python file: {e}'

    std_out = result.stdout.decode()
    std_err = result.stderr.decode()
    exit_code = result.returncode

    if not std_out and not std_err:
        return "No output produced"

    if exit_code != 0:
        return(f"\nSTDOUT: {std_out}\nSTDERR: {std_err}\nProcess exited with code {exit_code}")

    return f"\nSTDOUT: {std_out}\nSTDERR: {std_err}\n"