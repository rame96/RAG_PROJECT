# 🧠 RAG & AI Agents Workspace

A curated collection of Retrieval-Augmented Generation (RAG) pipelines, conversational agents, and vector database experiments. This repository serves as a central hub exploring different vector stores, document chunking techniques, memory frameworks, and LLM providers.

---

## 📂 Project Catalog

| Project | Vector DB | LLM / Embeddings | Key Tools & Libraries | Interface |
| :--- | :--- | :--- | :--- | :--- |
| **[`chat_bot_lance_DB`](./chat_bot_lance_DB)** | LanceDB | OpenAI (`gpt-4o-mini`, `text-embedding-3-small`) | IBM Docling, Tiktoken | Streamlit Web App |
| **[`RAG_Pipline`](./RAG_Pipline)** | Qdrant | Mistral AI (`mistral-large`, `mistral-embed`) | LangChain, PyPDF, Docker | CLI / Script |
| **[`Memory_Agent`](./Memory_Agent)** | Qdrant | Mistral AI | Mem0, LangChain | Python API / Script |
| **[`RAG_WITH_CROMA_db`](./RAG_WITH_CROMA_db)** | ChromaDB | Local / Default | ChromaDB Python Client | Jupyter Notebook |

---

## 🚀 Projects Overview

### 1. [chat_bot_lance_DB](./chat_bot_lance_DB) — Document Q&A Chatbot
An end-to-end, multi-modal document RAG pipeline with a polished Streamlit interface:
- **Parser**: Uses **IBM Docling** for advanced layout analysis, table parsing, and structure extraction from PDFs and web pages.
- **Chunking**: Token-aware hierarchical chunking via `HybridChunker` and `tiktoken`.
- **Vector Store**: Embedded serverless **LanceDB** (`docling.lance`).
- **Interactive UI**: Streamlit web chat with streaming responses and expandable source/page citations.
- **Entry Point**: `streamlit run chat_bot_lance_DB/5_chat.py`

### 2. [RAG_Pipline](./RAG_Pipline) — PDF Q&A with Qdrant & Mistral
A modular RAG workflow designed for document ingestion and context-grounded retrieval:
- **Ingestion**: Splits PDF documents (`Company_Data.pdf`) using LangChain's `RecursiveCharacterTextSplitter`.
- **Vector Store**: Local **Qdrant** instance running via Docker Compose (`docker-compose.yaml`).
- **Reasoning**: Generates answers strictly grounded in retrieved chunks using **Mistral AI** (`mistral-large-latest`) with page-number citations.
- **Entry Points**: 
  - Ingestion: `python RAG_Pipline/indexing.py`
  - Query: `python RAG_Pipline/retrival.py`

### 3. [Memory_Agent](./Memory_Agent) — Long-Term Conversational Memory
An implementation exploring personalized and persistent memory for AI agents:
- **Framework**: Built with **Mem0** (`mem0ai`).
- **Storage**: Backed by a local **Qdrant** vector store to persist user interactions and context.
- **LLM & Embedder**: Powered by **Mistral AI** (`mistral-embed` and `mistral-large-latest`).
- **Entry Point**: `Memory_Agent/memory.py`

### 4. [RAG_WITH_CROMA_db](./RAG_WITH_CROMA_db) — ChromaDB Prototyping
An experimental notebook for testing vector database operations:
- Hands-on testing of **ChromaDB** client modes (in-memory vs. persistent storage).
- Collection creation, document indexing, and querying experiments.
- **Entry Point**: `RAG_WITH_CROMA_db/croma_db.ipynb`

---

## 🛠️ Getting Started

### 1. Prerequisites
- **Python 3.10+** (recommended)
- **Docker & Docker Compose** (for running Qdrant in `RAG_Pipline` and `Memory_Agent`)
- API keys:
  - [OpenAI API Key](https://platform.openai.com/)
  - [Mistral AI API Key](https://console.mistral.ai/)

### 2. Virtual Environment Setup
```powershell
# Create and activate virtual environment
python -m venv ai_venv
.\ai_venv\Scripts\Activate.ps1

# Install base dependencies
pip install -r requirements.txt
```

### 3. Environment Variables
Create a `.env` file in the root directory (or inside individual project folders as needed):

```env
OPENAI_API_KEY="your-openai-api-key"
MISTRAL_API_KEY="your-mistral-api-key"
```

### 4. Running Local Qdrant (Optional)
If running `RAG_Pipline` or `Memory_Agent`:
```powershell
cd RAG_Pipline
docker-compose up -d
```
Qdrant Web UI will be accessible at: `http://localhost:6333/dashboard`

---

## 📌 Repository Structure

```text
RAG_PROJECT/
├── chat_bot_lance_DB/         # Docling + LanceDB + Streamlit RAG
│   ├── 1_data_extraction.ipynb
│   ├── 2_chunking.ipynb
│   ├── 3_embedding.ipynb
│   ├── 4_semantic_search.ipynb
│   └── 5_chat.py
├── RAG_Pipline/               # LangChain + Qdrant + Mistral RAG
│   ├── Company_Data.pdf
│   ├── docker-compose.yaml
│   ├── indexing.py
│   └── retrival.py
├── Memory_Agent/              # Mem0 conversational memory agent
│   └── memory.py
├── RAG_WITH_CROMA_db/         # ChromaDB prototyping notebook
│   └── croma_db.ipynb
├── .gitignore                 # Configured for virtualenvs, caches, vector DBs
├── requirements.txt           # Workspace requirements
└── README.md                  # This file
```
