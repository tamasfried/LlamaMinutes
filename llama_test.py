from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3.2:1b")

response = llm.invoke("Summarize the history of the Roman Empire in a single sentence.")

print(response)

