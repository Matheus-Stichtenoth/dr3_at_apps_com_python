from langchain.agents import Tool, create_react_agent, AgentExecutor
from langchain_google_genai import GoogleGenerativeAI
from langchain_openai.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from football_stats.matches import get_match_events
import pandas as pd
import json
import os
from dotenv import load_dotenv
from statsbombpy import sb

load_dotenv()

openai_key = os.environ['OPENAI_KEY']

def load_agent() -> AgentExecutor:
    """
    Configura o agente LangChain para responder perguntas sobre os eventos de uma partida específica.
    """
    def fetch_match_events():
        """
        Recebe o ID (string), converte para int e usa a função real get_match_events.
        """
        try:
            events = sb.events(match_id='22912')
            result = events.to_json()
            # Opcional: transformar a string JSON em texto amigável
            try:
                events = json.loads(result)
            except json.JSONDecodeError:
                return f"Retorno não é um JSON válido: {result}"

            if not events:
                return "Nenhum evento encontrado para essa partida."

            # Monta um resumo textual
            summary_lines = []
            for ev in events:
                minute = ev.get("minute", "N/A")
                event_type = ev.get("type", "N/A")
                team = ev.get("team", "N/A")
                outcome = ev.get("outcome", "")
                summary_lines.append(f"Min {minute}: {event_type} ({outcome}) - {team}")

            summary = "Eventos da partida (do JSON):\n" + "\n".join(summary_lines)
            return summary

        except Exception as e:
            return f"Erro ao buscar eventos: {str(e)}"

    get_events_tool = Tool(
        name="GetMatchEvents",
        func=fetch_match_events,
        description="Carrega os eventos principais da partida de futebol entre Liverpool e Tottenham Hotspur na final da Champions League de 2019.",
        return_direct=False
    )

    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo",  # Pode usar gpt-4 se tiver acesso
        openai_api_key=openai_key,
        temperature=0.2
    )

    # Prompt que enfatiza que a ferramenta é REAL e deve ser utilizada
    prompt_template = PromptTemplate(
        input_variables=["input", "match_id", "agent_scratchpad", "tool_names", "tools"],
        template="""
        [System: Você é um assistente que TEM ACESSO a uma função real GetMatchEvents. Essa função retorna dados JSON verdadeiros sobre a partida especificada. Confie na ferramenta e utilize-a quando necessário.]

        Thought: think about what to do
        Action: one of {tool_names}
        Action Input: read the data
        Observation: the tool's response
        Thought: your final reasoning
        Final Answer: your final answer

        Ferramentas disponíveis:
        {tool_names}

        Descrições das ferramentas:
        {tools}

        Pergunta do usuário:
        {input}

        Seu pensamento até agora (chain-of-thought):
        {agent_scratchpad}

        [Instruções: SE você precisar de informações sobre o número de gols ou eventos, use a ferramenta GetMatchEvents com o ID fornecido. Caso contrário, responda diretamente.]

        Agora responda de forma precisa e detalhada, usando os dados da ferramenta quando necessário.
                """
            )

    agent = create_react_agent(llm, tools=[get_events_tool], prompt=prompt_template)

    return AgentExecutor(
        agent=agent,
        tools=[get_events_tool],
        handle_parsing_errors=True,
        verbose=True,
        max_iterations=10
    )