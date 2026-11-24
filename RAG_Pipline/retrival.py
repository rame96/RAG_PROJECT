from langchain_mistralai import MistralAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

llm = ChatMistralAI(model="mistral-large-latest")

embeddings = MistralAIEmbeddings(
    model="mistral-embed",
)

qdrant = QdrantVectorStore.from_existing_collection(
    embedding=embeddings,
    url="http://localhost:6333",
    prefer_grpc=False,
    collection_name="my_documents",
)

querry = input("how can i help you: ")

search_result = qdrant.similarity_search(query=querry)

# Build context
context = ""

for doc in search_result:
    print("Page:", doc.metadata.get("page"))
    print("Content:", doc.page_content[:200], "...")
    context += f"Page {doc.metadata['page']}: {doc.page_content}\n\n"

SYSTEM_PROMPT = f"""
You are a helpful assistant. You give answers based on the available context retrieved from PDF files.
Always provide page numbers so the user can check for more information.

Contect:
{context}
"""


messages = [
    SystemMessage(content=SYSTEM_PROMPT),
    HumanMessage(content=f"Question: {querry}")
]

# Generate answer
response = llm.generate([messages])  # Pass a list of conversations

# Extract text
answer = response.generations[0][0].text
print(answer)
