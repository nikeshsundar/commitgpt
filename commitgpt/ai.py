import os
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

class AIError(RuntimeError):
    pass

def get_api_key() -> str:
    key = os.getenv("OPENAI_API_KEY")
    if key:
        return key
    
    load_dotenv()
    key = os.getenv("OPENAI_API_KEY")
    if key:
        return key
    
    config_path = Path.home() / ".commitgpt"
    if config_path.exists():
        key = config_path.read_text().strip()
        if key:
            return key
            
    raise AIError("OPENAI_API_KEY environment variable is not set, and ~/.commitgpt is missing or empty.")


def generate_text(system_prompt: str, user_prompt: str, emoji: bool = False) -> str:
    try:
        api_key = get_api_key()
        client = OpenAI(api_key=api_key)
        
        if emoji:
            system_prompt += "\nAlso add an appropriate emoji at the start of the commit message."
            
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.3,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        raise AIError(f"OpenAI API Error: {str(e)}")
