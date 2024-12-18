import streamlit as st
from football_stats.matches import get_match_events, summarize_events
from tools.summarization import generate_summary
import pandas as pd
import json
import statsbombpy as sb


def func_narracao():
    """
    Retorna a pagina de narração onde o usuário ira selecionar uma narração, com streamlit
    """
    st.title("Análise de Partida de Futebol ⚽")


    match_id = st.sidebar.number_input("Digite o ID da partida", min_value=1)
    style = st.sidebar.selectbox("Escolha o estilo de narração", ["Formal", "Humorística", "Técnica"])

    if st.sidebar.button("Analisar"):
        events = get_match_events(match_id)
        summary = summarize_events(pd.DataFrame(json.loads(events)))
        final_summary = generate_summary(events_summary=summary,style=style)

        st.subheader("Sumarização dos Eventos")
        st.write(final_summary)