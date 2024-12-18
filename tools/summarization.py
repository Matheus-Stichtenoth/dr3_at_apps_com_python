from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_google_genai import GoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv('.env')
gemini_key = os.environ["GEMINI_KEY"]

def generate_summary(events_summary: str, style: str) -> str:
    """
    Gera uma narrativa utilizando LLM.
    """
    template = """
    Baseado nos eventos da partida fornecidos:
    {events_summary}

    Crie uma descrição amigável e detalhada do jogo, utilizando o seguinte tom para a narração:
    {style}
    """
    prompt = PromptTemplate.from_template(template)
    llm = GoogleGenerativeAI(model="gemini-1.5-flash", api_key=gemini_key)
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(events_summary=events_summary, style= style)