from mem0 import Memory
from langchain_mistralai import MistralAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv

load_dotenv()


config = {
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "collection_name": "test",
            "host": "localhost",
            "port": 6333,
        }
    },

    "llm": {
        "provider": "MistralAI",
        "config": {"model": "mistral-large-latest"}
    },

    "embedder": {
        "provider": "MistralAI",
        "config": {"model": "mistral-embed"}
    }
}

mem_client = Memory.from_config(config)

