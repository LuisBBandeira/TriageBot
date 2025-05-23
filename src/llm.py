# import litellm
from langchain_openai import ChatOpenAI
from crewai import LLM
import os

# Configure environment
os.environ["OPENAI_API_KEY"] = "sk-ollama"
# litellm._turn_on_debug()

# def get_gemma2():
#     """
#     Returns a configured LangChain ChatOpenAI instance for the Gemma 2B model via Ollama.
#     """
#     return ChatOpenAI(
#         model='gemma:2b',
#         base_url="http://ollama:11434",
#         model_kwargs={"provider": "ollama"},
#         temperature=0.7,
#         max_tokens=1024
#     )

def get_llma_llm():
    llm = LLM(
    model="ollama/tinyllama",
    base_url="http://ollama:11434"
    )
    return llm
