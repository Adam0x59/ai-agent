import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import *
from functions.call_function import *
from functions.function_definitions import *

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

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info, schema_get_file_content, schema_run_python_file, schema_write_file,
    ]
)

iteration_count = 0
while iteration_count <= 20:
    iteration_count += 1
    
    response = client.models.generate_content(
        model = 'gemini-2.0-flash-001', 
        contents = messages,
        config = types.GenerateContentConfig(tools=[available_functions], system_instruction=SYSTEM_PROMPT)
    )

    if response.function_calls:
        for item in response.candidates:
            messages.append(item.content)
        is_verbose = "--verbose" in flags
        for function_call_part in response.function_calls:
            
            # Call the function
            function_call_result = call_function(function_call_part, verbose=is_verbose)
            
            # raise Exception if the function call generates an incorrect output
            if not (hasattr(function_call_result, 'parts') and
                len(function_call_result.parts) > 0 and
                hasattr(function_call_result.parts[0], 'function_response') and
                hasattr(function_call_result.parts[0].function_response, 'response')):
                raise Exception("Fatal Error: Unexpected function call result structure!")
            # If no error and flag is_verbose is True print the result
            elif is_verbose:    
                print(f"-> {function_call_result.parts[0].function_response.response}")
            # Append the result to messages
            messages.append(function_call_result)
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
        for item in response.candidates:
            messages.append(item.content)
        break
            #messages.append(function_call_result)
        

