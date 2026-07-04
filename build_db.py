from modules.vectorstore import build_vector_db

build_vector_db(
    "data/knowledge.pdf"
)

print("Vector database built successfully.")