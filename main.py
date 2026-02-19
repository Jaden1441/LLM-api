def main():
    import argparse
    import os 
    from dotenv import load_dotenv
    from google.genai import types

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key is None:
        raise RuntimeError('GEMINI_API_KEY')

    from google import genai

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()
    
    client = genai.Client(api_key = api_key)
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    response = client.models.generate_content(
        model="gemini-2.5-flash",contents=messages
        )
    
    usage = response.usage_metadata
    prompt_tokens = usage.prompt_token_count
    response_tokens = usage.candidates_token_count

    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Response tokens: {response_tokens}")
    print(f"\n{response.text}")
    

if __name__ == "__main__":
    main()