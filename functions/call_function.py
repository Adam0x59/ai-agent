from functions import get_files_info, get_files_content, write_file, run_python_file
from google.genai import types

def call_function(function_call_part, verbose=False):

    if verbose == True:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    function_name = function_call_part.name
    function_args = function_call_part.args
    function_args["working_directory"] = "calculator"

    funky_dict = {
        "get_files_info": get_files_info.get_files_info,
        "get_files_content": get_files_content.get_file_content,
        "run_python_file": run_python_file.run_python_file,
        "write_file": write_file.write_file,
    }

    if function_name not in funky_dict:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name} not in dict"},
                )
            ],
        )
    
    function_result = funky_dict[function_name](**function_args)

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )