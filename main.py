import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

verbose = False

def retrieve_prompt_argument() -> str:
    if len(sys.argv) < 2:
        print("Please provide a prompt argument")
        exit(1)
    elif len(sys.argv) == 2 and sys.argv[1] == "--verbose":
        print("Please provide a prompt argument")
        exit(1)
    
    if "--verbose" in sys.argv:
        global verbose 
        verbose = True

    return sys.argv[1]


if __name__ == "__main__":
    load_dotenv()

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = retrieve_prompt_argument()
    
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=messages
    )

    if verbose is True:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
