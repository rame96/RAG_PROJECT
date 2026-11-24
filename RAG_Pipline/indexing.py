from re import L
from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_mistralai import MistralAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv

load_dotenv()


pdf_path = Path(__file__).parent/"Company_Data.pdf"

file_path = pdf_path
loader = PyPDFLoader(file_path)
docs = loader.load()


#split the docs
text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=75)
chunks = text_splitter.split_documents(docs)

#embedding
embeddings = MistralAIEmbeddings(
    model="mistral-embed",
)

qdrant = QdrantVectorStore.from_documents(
    chunks,
    embeddings,
    url="http://localhost:6333",
    prefer_grpc=False,
    collection_name="my_documents",
)

print("done")