import streamlit as st
from app.agent import load_agent
from football_stats.matches import get_match_events  # se for realmente necessário
from langchain.schema import AIMessage, HumanMessage

def func_question():
    """
    Retorna a página criada para questões, com uso de react agent no streamlit
    """
    st.title("Perguntas sobre Partidas de Futebol ⚽")

    match_id = st.sidebar.number_input("Digite o ID da partida", min_value=1, step=1, format="%d")
    user_question = st.text_area("Faça uma pergunta sobre a partida", "")

    if st.button("Perguntar ao Agente"):
        if user_question and match_id > 0:
            with st.spinner("Consultando o agente..."):
                try:
                    agent_executor = load_agent()

                    input_data = {
                        "input": user_question,
                        "match_id": '22912',
                        "agent_scratchpad": "",
                    }

                    # Invoca o agente
                    response = agent_executor.invoke(input_data)

                    st.subheader("Resposta do Agente:")
                    if isinstance(response, dict) and "output" in response:
                        st.write(response["output"])
                    else:
                        st.write(response)

                except Exception as e:
                    st.error(f"Erro ao consultar o agente: {str(e)}")
        else:
            st.warning("Por favor, digite uma pergunta e um ID válido da partida.")