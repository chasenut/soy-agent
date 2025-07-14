import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def main():
    if len(sys.argv) < 2:
        print("Error, no prompt provided")
        sys.exit(1)
    model = "gemini-2.0-flash-001"
    user_prompt = sys.argv[1]
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    generated_content_response = client.models.generate_content(model=model, contents=messages)


    print(generated_content_response.text)
    if len(sys.argv) > 2 and sys.argv[2] == "--verbose":
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {generated_content_response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {generated_content_response.usage_metadata.candidates_token_count}")
        
if __name__ == "__main__":
    main()
