import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from prompts import system_prompt
from call_function import call_function, available_functions
from config import MODEL_NAME

def main():
    load_dotenv()
     
    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]
    
    if not args:
        print("Error, no prompt provided")
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    if verbose:
        print(f"User prompt: {user_prompt}\n")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    
    for i in range(20):
        try:
            result = generate_content(client, messages, verbose)
            if result:
                print("Result:")
                print(result)
                break
        except Exception as e:
            print(f"[ERROR]: {e}")

def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=messages,
        config=types.GenerateContentConfig(system_instruction=system_prompt,
                                           tools=[available_functions]),
    )
    for candidate in response.candidates:
        messages.append(candidate.content)

    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    if not response.function_calls:
        return response.text

    function_responses = []
    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose)
        if (
            not function_call_result.parts
            or not function_call_result.parts[0].function_response
        ):
            raise Exception("Empty function call result")
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
        function_responses.append(function_call_result.parts[0])

    if not function_responses:
        raise Exception("No function calls generated, exiting")

    messages.append(types.Content(
                                    parts=function_responses,
                                    role="tool"
    ))


if __name__ == "__main__":
    main()
