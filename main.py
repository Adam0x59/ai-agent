import os
import sys
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

try:
    prompt = sys.argv[1]
except IndexError:
    print('Please provide a prompt message.\nUsage: ./main.py <"Prompt message">')
    sys.exit(1)

response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents=f"{prompt}"
)
print(response.text)
print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

