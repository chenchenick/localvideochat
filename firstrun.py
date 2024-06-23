from langchain_community.llms import Ollama

def main():
    local_llm = "llama3"
    llm = Ollama(model=local_llm)
    # llm.invoke("why sky blue?")

    # Define the prompt you want to send to the LLM
    prompt = "What is the capital of France?"

    # Invoke the LLM and get the response
    try:
        response = llm.invoke(prompt)
        
        # Handle the return value (response)
        print("LLM response:", response)

    except Exception as e:
        print("Error invoking the LLM:", e)

if __name__ == "__main__":
    main()