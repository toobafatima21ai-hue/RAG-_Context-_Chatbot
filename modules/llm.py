import time

from langchain_community.llms import Ollama

llm = Ollama(
    model="mistral"
)

def ask_llm(prompt):

    start = time.time()

    response = llm.invoke(
        prompt
    )

    print(
        f"LLM Generation Time: {time.time() - start:.2f} sec"
    )

    return response