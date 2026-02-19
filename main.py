def main():
    import os 
    from dotenv import load_dotenv

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key is None:
        raise RuntimeError('GEMINI_API_KEY')

    from google import genai

    
    client = genai.Client(api_key = api_key)
    response = client.models.generate_content(model="gemini-2.5-flash",contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum." )
    
    usage = response.usage_metadata
    prompt_tokens = usage.prompt_token_count
    response_tokens = usage.candidates_token_count

    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Response tokens: {response_tokens}")
    print(f"\n{response.text}")
    

if __name__ == "__main__":
    main()