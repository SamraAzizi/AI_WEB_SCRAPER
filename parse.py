from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = (
    "You are tasked with extraction specific information from the following text context {dom_context}."
    "Please follow these instruction carefully : \n\n"
    "1. **Extract Information:** Only extract the information directly matches the provided description: {parse_description}"
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text.""

)

model = OllamaLLM(model="llama2")

def parse_with_ollama(dom_chunks, parse_description):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt  | model
    
    parsed_result = []

    for i, chunk in enumerate(dom_chunks, start=1):
        response = chain.invoke(
            {"dom_content": chunk, "paser_description":parse_description}
        )
