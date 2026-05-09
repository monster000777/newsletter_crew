from typing import Optional
import os
from dotenv import load_dotenv

load_dotenv()

def get_config(key: str, default: Optional[str] = None) -> Optional[str]:
    return os.getenv(key, default)

OPENAI_API_KEY = get_config("OPENAI_API_KEY")
OPENAI_BASE_URL = get_config("OPENAI_BASE_URL", "https://api.openai.com/v1")
OPENAI_MODEL = get_config("OPENAI_MODEL", "gpt-4o")
SERPER_API_KEY = get_config("SERPER_API_KEY")
