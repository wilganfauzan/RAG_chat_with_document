import os

from chromadb import HttpClient
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

chroma = HttpClient(host="localhost", port=8010)

openai_ef = OpenAIEmbeddingFunction(
    api_key=os.getenv("OPENAI_API_KEY"), model_name="text-embedding-3-small"
)
