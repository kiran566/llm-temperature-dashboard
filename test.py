from llm import generate_response
result = generate_response(
    "Explain RAG in one sentence.",
    temperature=0,
    top_p=1,
    max_tokens=100
)

print(result["text"])