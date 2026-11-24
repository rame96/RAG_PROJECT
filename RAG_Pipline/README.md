Retrieval-Augmented Generation (RAG) with Qdrant & Mistral

This project implements a Retrieval-Augmented Generation (RAG) pipeline that allows you to ask questions about PDF documents and receive context-grounded answers with page references.

The system:

Extracts text from PDFs

Splits text into chunks

Stores embeddings in Qdrant

Retrieves relevant chunks using similarity search

Uses Mistral LLM to generate answers strictly from retrieved context

🚀 Features

✅ PDF-based question answering

✅ Vector search using Qdrant

✅ Dense embeddings via MistralAIEmbeddings

✅ Page-number aware responses

✅ Fully local vector database (no cloud DB required)

✅ Debug-friendly & modular code
