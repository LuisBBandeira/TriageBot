from src.llm import get_llma_llm
from langchain.schema import HumanMessage

def main():
    llm = get_llma_llm()
    prompt = "Say hello. Respond with a single word."
    messages = [HumanMessage(content=prompt)]
    
    try:
        response = llm.invoke(messages)
        print("LLM response:", response.content)
    except Exception as e:
        print(f"Error calling LLM: {e}")

if __name__ == "__main__":
    main()
