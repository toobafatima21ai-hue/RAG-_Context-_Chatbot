from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS


def build_vector_db(pdf_path="data/knowledge.pdf"):

    loader = PyPDFLoader(pdf_path)

    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(docs)

    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )

    db = FAISS.from_documents(
        chunks,
        embeddings
    )

    db.save_local(
        "vectordb/faiss_index"
    )

    print("✅ Vector database created successfully.")