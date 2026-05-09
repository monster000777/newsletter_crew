# 配置管理模块
import os
from dotenv import load_dotenv

load_dotenv()

def get_config(key: str, default: str = None) -> str:
    return os.getenv(key, default)

# 环境变量
OPENAI_API_KEY = get_config("OPENAI_API_KEY")
OPENAI_BASE_URL = get_config("OPENAI_BASE_URL", "https://api.openai.com/v1")
OPENAI_MODEL = get_config("OPENAI_MODEL", "gpt-4o")
SERPER_API_KEY = get_config("SERPER_API_KEY")
