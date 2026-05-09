"""配置管理模块"""
from typing import Optional
import os
from dotenv import load_dotenv

load_dotenv()


def get_config(key: str, default: Optional[str] = None) -> Optional[str]:
    """获取环境变量"""
    return os.getenv(key, default)


OPENAI_BASE_URL: str = get_config("OPENAI_BASE_URL", "https://api.openai.com/v1")
OPENAI_MODEL: str = get_config("OPENAI_MODEL", "gpt-4o")
SERPER_API_KEY: Optional[str] = get_config("SERPER_API_KEY")
