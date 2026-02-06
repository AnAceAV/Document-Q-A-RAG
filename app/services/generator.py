from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="phi", base_url="http://localhost:11434")

def generate_answer(context_chunks, question):
    context = "\n".join(context_chunks)
    prompt = f"""Based on the following document content, answer the question concisely and accurately.

Document:
{context}

Question: {question}

Answer:"""
    
    answer = llm.invoke(prompt)
    return answer
