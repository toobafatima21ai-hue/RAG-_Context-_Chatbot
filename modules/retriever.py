from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS


def get_retriever():

    embeddings = OllamaEmbeddings(
        model="nomic-embed-text",
        base_url="http://localhost:11434"
    )

    db = FAISS.load_local(
        "vectordb/faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    return db.as_retriever(
        search_kwargs={"k": 1}
    )