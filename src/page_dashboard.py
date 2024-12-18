import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt
from mplsoccer import Pitch, Sbopen
from statsbombpy import sb
import time

def image_icones (url:str, tamanho = 100) -> None:
    st.image(url, width=tamanho)

def align_text(text:str, h:str = 'h6', align:str = 'center') -> None:
    st.markdown(f'<{h} style = "text-align: {align};">{text}</{h}>', unsafe_allow_html=True)

def func_dashboard() -> None:
    st.title('Resultados de Partidas ⚽')

    competitions = sb.competitions()
    competitions_names = competitions['competition_name'].unique()
    comp = st.selectbox('Selecione a competição ⬇:',competitions_names)
    comp_id = competitions[competitions['competition_name'] == comp]['competition_id'].values[0]

    seasons = competitions[competitions['competition_id'] == comp_id]['season_name'].unique()
    season_name = st.selectbox(f'Selecione a temporada da Competição {comp}:',seasons)
    season_id = competitions[competitions['season_name'] == season_name]['season_id'].values[0]

    matches = sb.matches(competition_id=comp_id,season_id = season_id)
    def get_match_label(match_id):
        row = matches[matches['match_id'] == match_id].iloc[0]
        return f'{row['match_date']} - {row['home_team']} vs {row['away_team']}'
    game = st.selectbox(f'Selecione uma Partida da Competição {comp} | Temporada: {season_name}',matches['match_id'],format_func = get_match_label)

    align_text(text='Aguarde os cards de dribles e passes aparecerem, para dar sequência na sua navegação 😁')

    total_goals = matches['home_score'].sum() + matches['away_score'].sum()

    total_partidas = matches.shape[0]

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric('Partidas no Campeonato*', total_partidas)

    with c2:
        st.metric('Gols no Campeonato*',total_goals)

    with c3:
        total_dribles = 0
        for i in range(len(matches)):
            drible_partida = sb.events(match_id=matches['match_id'][i], split=True, flatten_attrs=False)["dribbles"]
            qtd_dribles = drible_partida.shape[0]
            total_dribles += qtd_dribles

        st.metric('Dribles no Campeonato*',total_dribles)
    
    with c4:
        total_pass = 0
        for i in range(len(matches)):
            pass_partida = sb.events(match_id=matches['match_id'][i], split=True, flatten_attrs=False)["passes"]
            qntd_pass = pass_partida.shape[0]
            total_pass += qntd_pass

        st.metric('Passes no Campeonato*',total_pass)

    st.subheader(f'Competição {comp} | Temporada: {season_name}')

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        image_icones('https://cdn-icons-png.freepik.com/512/11818/11818132.png', tamanho = 50)

    with c2:
        arbitro = matches[matches['match_id'] == game]['referee'].values[0]
        st.markdown(f'<h5 style = "text-align: left;">{arbitro}</h5>', unsafe_allow_html=True)

    lc, rc = st.columns(2)
    with lc:
        st.write('Time da Casa')
        image_icones('https://cdn-icons-png.flaticon.com/256/88/88961.png')
        home_team = matches[matches['match_id'] == game]['home_team'].values[0]
        st.subheader(home_team)
        home_score = matches[matches['match_id'] == game]['home_score'].values[0]
        st.metric('Gols Marcados',home_score)

    with rc:
        st.write('Time Visitante')
        image_icones('https://cdn-icons-png.flaticon.com/256/912/912834.png')
        away_team = matches[matches['match_id'] == game]['away_team'].values[0]
        st.subheader(away_team)
        away_score = matches[matches['match_id'] == game]['away_score'].values[0]
        st.metric('Gols Marcados',away_score)

    st.header('Dados da Partida')

    dribles_partida = sb.events(match_id=game, split=True, flatten_attrs=False)["dribbles"]

    passes_partida = sb.events(match_id=game, split=True, flatten_attrs=False)["passes"]

    chutes_partida = sb.events(match_id=game, split=True, flatten_attrs=False)["shots"]

    chutes_c, passes_c, dribles_c = st.columns(3)

    with chutes_c:
        st.subheader('Chutes Realizados na Partida')
        st.dataframe(chutes_partida.drop(columns=['id','index']))

        if st.checkbox('Deseja efetuar o download dos dados de chutes?'):
            progress_bar = st.progress(0)
            for counter in range (1,101):
                time.sleep(0.015)
                progress_bar.progress(counter)
            with st.spinner('Carregando arquivo...'):
                time.sleep(3)

            st.download_button(label = 'Clique aqui para baixar os dados de chutes!',
                            data = chutes_partida.drop(columns=['id','index']).to_csv(index=False),
                            file_name= f'dados_chutes.csv')
    
    with passes_c:
        st.subheader('Passes Realizados na Partida')
        st.dataframe(passes_partida.drop(columns=['id','index']))
        if st.checkbox('Deseja efetuar o download dos dados de passes?'):
            progress_bar = st.progress(0)
            for counter in range (1,101):
                time.sleep(0.015)
                progress_bar.progress(counter)
            with st.spinner('Carregando arquivo...'):
                time.sleep(3)

            st.download_button(label = 'Clique aqui para baixar os dados de passes!',
                            data = passes_partida.drop(columns=['id','index']).to_csv(index=False),
                            file_name= f'dados_passes.csv')
    
    with dribles_c:
        st.subheader('Dribles Realizados na Partida')
        st.dataframe(dribles_partida.drop(columns=['id','index']))
        if st.checkbox('Deseja efetuar o download dos dados de dribles?'):
            progress_bar = st.progress(0)
            for counter in range (1,101):
                time.sleep(0.015)
                progress_bar.progress(counter)
            with st.spinner('Carregando arquivo...'):
                time.sleep(3)

            st.download_button(label = 'Clique aqui para baixar os dados de dribles!',
                            data = dribles_partida.drop(columns=['id','index']).to_csv(index=False),
                            file_name= f'dados_dribless.csv')