from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

schema_get_file_content = types.FunctionDeclaration(
    name="get_files_content",
    description="Get the content of a specific file which exists in the working directory, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path of the file to get contents from which exists in the working directory, relative to the working directory. If not provided, or not a file an error will be raised.",
            ),
        },
    ),
)

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run a specific python file which exists in the working directory, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path of the file to run which exists in the working directory, relative to the working directory. If not provided, or not a python file (.py) an error will be raised.",
            ),
        },
    ),
)

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="write to a file in the working directory, if the file exists already it will be cleared and overwritten, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path of the file to write to which exists in the working directory, relative to the working directory. If not provided, an error will be raised. If containig directory does not exist it will be created, so lomg as it is in the working directory (relative paths only)",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="A string of text content which will be written to the provided file_path."
            )
        },
    ),
)