from modules.retriever import get_retriever
from modules.llm import ask_llm

retriever = get_retriever()


def chatbot_response(user_query):

    print("✅ Question received")

    docs = retriever.invoke(user_query)

    print("✅ Documents retrieved")

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    sources = []

    for doc in docs:

        page = doc.metadata.get(
            "page",
            "Unknown"
        )

        sources.append(
            f"Page {page}"
        )

    prompt = f"""
You are a helpful AI assistant.

Answer only using the context.

Context:
{context}

Question:
{user_query}
"""

    print("✅ Sending prompt to Mistral")

    answer = ask_llm(prompt)

    print("✅ Response received")

    return answer, context, sources