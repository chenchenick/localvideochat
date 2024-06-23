from langchain_community.llms import Ollama

def process_message(user_message):
    local_llm = "llama3"
    llm = Ollama(model=local_llm)
    response = llm.invoke(user_message)
    # Simple echo for now
    return response