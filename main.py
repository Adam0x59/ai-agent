import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import *
from functions.call_function import *

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


try:
    user_prompt = sys.argv[1]
except IndexError:
    print('Please provide a prompt message.\nUsage: ./main.py <"Prompt message">')
    sys.exit(1)

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

try:
    flags = sys.argv[2:]
except IndexError:
    print("No flags specified, continuing...")
    pass

# Function Definitions
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

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info, schema_get_file_content, schema_run_python_file, schema_write_file,
    ]
)

response = client.models.generate_content(
    model = 'gemini-2.0-flash-001', 
    contents = messages,
    config = types.GenerateContentConfig(tools=[available_functions], system_instruction=SYSTEM_PROMPT)
)

if response.function_calls:
    if "--verbose" in flags:
        for function_call_part in response.function_calls:
            function_call_result = call_function(function_call_part, verbose=True)
            if not (hasattr(function_call_result, 'parts') and
                    len(function_call_result.parts) > 0 and
                    hasattr(function_call_result.parts[0], 'function_response') and
                    hasattr(function_call_result.parts[0].function_response, 'response')):
                    raise Exception("Fatal Error: Unexpected function call result structure!")
            print(f"-> {function_call_result.parts[0].function_response.response}")
    else:
        for function_call_part in response.function_calls:
            function_call_result = call_function(function_call_part)
            if not (hasattr(function_call_result, 'parts') and
                    len(function_call_result.parts) > 0 and
                    hasattr(function_call_result.parts[0], 'function_response') and
                    hasattr(function_call_result.parts[0].function_response, 'response')):
                    raise Exception("Fatal Error: Unexpected function call result structure!")
            
else:
    if "--verbose" in flags:
        print(f"User prompt: {user_prompt}")
        print("------------------")
        print(response.text)
        print("------------------")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        print("------------------")
    else:
        print(response.text)
