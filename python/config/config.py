BASE_URL = 'https://ark.cn-beijing.volces.com/api/v3'
API_KEY = "f3c853c7-2505-4219-b9d5-73f4a945707a"
MODEL_NAME = 'deepseek-v3-250324'
PROJECT_PATH = "D://PYTHON//MCP-Manager//python"

OLLAMA_URL="http://119.3.125.66:11434"
EMBEDDING_MODEL="bge-m3:567m"

if EMBEDDING_MODEL == "dengcao/Qwen3-Embedding-0.6B:F16":
    EMBEDDING_CACHE_FILE = f"{PROJECT_PATH}//data//embedding//embedding_qwen3_0.6b.jsonl"
elif EMBEDDING_MODEL == "bge-m3:567m":
    EMBEDDING_CACHE_FILE = f"{PROJECT_PATH}//data//embedding//embedding_bge_m3.jsonl"
else:
    raise ValueError("Invalid EMBEDDING_MODEL")

DB_TYPE = "chroma"
#DB_TYPE = "faiss"
