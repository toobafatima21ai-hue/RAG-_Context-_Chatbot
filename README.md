# 🤖 Context-Aware RAG Chatbot

A professional Retrieval-Augmented Generation (RAG) chatbot that enables users to interact with their own PDF documents using semantic search and local Large Language Models (LLMs). The system retrieves relevant document content from a FAISS vector database and generates context-aware responses using Ollama-powered Mistral.

---

## 📌 Overview

This project combines document retrieval and generative AI to create an intelligent chatbot capable of answering questions from user-provided PDF documents. By leveraging vector embeddings and similarity search, the chatbot grounds its responses in the uploaded knowledge base, reducing hallucinations and improving answer relevance.

---

## ✨ Features

* 📄 Upload and analyze custom PDF documents
* 🔍 Semantic search using vector embeddings
* 🧠 Retrieval-Augmented Generation (RAG)
* 🤖 Local LLM inference with Ollama + Mistral
* ⚡ Fast document retrieval using FAISS
* 💬 Interactive chat interface built with Streamlit
* 📚 Retrieved context visualization
* 📄 Source page references
* 📝 Chat export to TXT and PDF formats
* 🎨 Modern and responsive user interface
* 🔒 Fully local AI workflow (no external API required)

---

## 🏗️ System Architecture

```text
PDF Document
      │
      ▼
Document Loader (PyPDF)
      │
      ▼
Text Chunking
      │
      ▼
Embeddings (nomic-embed-text)
      │
      ▼
FAISS Vector Database
      │
      ▼
Retriever
      │
      ▼
Mistral (Ollama)
      │
      ▼
Generated Response
```

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Retrieval Layer

* LangChain
* FAISS

### Embedding Model

* Ollama Embeddings
* nomic-embed-text

### Language Model

* Ollama
* Mistral

### Document Processing

* PyPDFLoader
* RecursiveCharacterTextSplitter

### Export Utilities

* ReportLab
* TXT Export

---

 

---

 
## 💡 Usage

1. Launch the application.
2. Upload a PDF document.
3. Wait for vector database creation.
4. Ask questions related to the document.
5. Review retrieved context and source pages.
6. Export conversations if needed.

---

## 🎯 Example Questions

* What is the main topic of this document?
* Summarize chapter 3.
* What are the key findings of the research?
* Explain the methodology used.
* What conclusions were drawn?

---

## 🔒 Advantages of RAG

* Reduces hallucinations
* Provides document-grounded answers
* Supports custom knowledge bases
* Improves response accuracy
* Enables scalable document search

---

## 📈 Future Enhancements

* Multi-document knowledge base
* Conversational memory persistence
* Multiple file uploads
* Hybrid search (keyword + vector)
* User authentication
* Cloud deployment
* Citation highlighting
* Real-time document indexing

---

## 👨‍💻 Author
tooba fatima

---

## 📜 License

This project is intended for educational, research, and portfolio purposes.
