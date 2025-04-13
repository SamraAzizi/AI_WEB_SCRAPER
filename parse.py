from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = (
    "You are tasked with extraction specific information from the following text context {dom_context}."
    "Please follow these instruction carefully : \n\n"
    "1. **Extract Information:** Only extract "

)

model = OllamaLLM(model="llama2")

def parse_with_ollama(dom_chunks, parse_description):
