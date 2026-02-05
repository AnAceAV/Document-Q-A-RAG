def generate_answer(context_chunks, question):
    context = "\n".join(context_chunks)
    return f"Based on the document:\n{context}\n\nAnswer: {question}"
