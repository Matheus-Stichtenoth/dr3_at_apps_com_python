import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt
from mplsoccer import Pitch, Sbopen
from statsbombpy import sb

parser = Sbopen()

def align_text(text:str, h:str = 'h6', align:str = 'center') -> None:
    st.markdown(f'<{h} style = "text-align: {align};">{text}</{h}>', unsafe_allow_html=True)

def center_img (url:str, altura:str = '100', largura:str = '300') -> None:
    st.markdown(f'''
    <div style="text-align: center;">
        <img src="{url}" alt= "-" />
        
    </div>
''', unsafe_allow_html=True)

def match_data(match_id):
    return parser.event(match_id)[0]

def image_icones (url:str, tamanho = 100) -> None:
    st.image(url, width=tamanho)

def plot_passes(match, player_name) -> None:
    player_filter = (match.type_name == 'Pass') & (match.player_name == player_name)
    df_pass = match.loc[player_filter, ['x', 'y', 'end_x', 'end_y']]
    pitch = Pitch(line_color='black', pitch_color='#799351', stripe_color='#799351', stripe=True)
    fig, ax = pitch.grid(grid_height=0.9, title_height=0.06, axis=False, endnote_height=0.04, title_space=0, endnote_space=0)
    pitch.arrows(df_pass.x, df_pass.y, df_pass.end_x, df_pass.end_y, color='white', ax=ax['pitch'])
    #pitch.kdeplot(x=df_pass.x, y=df_pass.y, ax=ax['pitch'], alpha=0.5, shade=True, cmap='plasma')
    return fig

def plot_shot(match, player_name) -> None:
    player_filter = (match.type_name == 'Shot') & (match.player_name == player_name)
    df_pass = match.loc[player_filter, ['x', 'y', 'end_x', 'end_y']]
    pitch = Pitch(line_color='black', pitch_color='#799351', stripe_color='#799351', stripe=True)
    fig, ax = pitch.grid(grid_height=0.9, title_height=0.06, axis=False, endnote_height=0.04, title_space=0, endnote_space=0)
    pitch.arrows(df_pass.x, df_pass.y, df_pass.end_x, df_pass.end_y, color='white', ax=ax['pitch'])
    #pitch.kdeplot(x=df_pass.x, y=df_pass.y, ax=ax['pitch'], alpha=0.5, shade=True, cmap='plasma')
    return fig

def func_jogador() -> None:
    st.title('Estatísticas do Jogador 👤')
    align_text(text = 'Comparativo Na Final da Champions League 2009',h = 'h3')
    align_text(text = 'Barcelona x Manchester United',h = 'h2')
    align_text(text = 'Lionel Messi x Cristiano Ronaldo',h = 'h3')
    
    escalacao = ('https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Barcelona_vs_Man_Utd_2009-05-27.svg/800px-Barcelona_vs_Man_Utd_2009-05-27.svg.png')
    center_img(escalacao)
    
    messi_photo, mid, mid2, cr7_photo = st.columns(4)

    cl_2009 = sb.matches(competition_id=16,season_id=41)
    id_cl_2009 = cl_2009[(cl_2009['home_team']=='Barcelona') & (cl_2009['away_team'] == 'Manchester United')].match_id.values[0]
    final_data = match_data(id_cl_2009)

    cl_final = sb.events(match_id=id_cl_2009)

    messi_name = 'Lionel Andrés Messi Cuccittini'
    cris_name = 'Cristiano Ronaldo dos Santos Aveiro'

    with messi_photo:
        st.subheader('Messi')
        image_icones('https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/2a0c257d-1e26-439e-8561-e67976a7a2e4/deb9rhf-a28db2f2-263b-45b2-9bbd-a7894cd6e133.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzJhMGMyNTdkLTFlMjYtNDM5ZS04NTYxLWU2Nzk3NmE3YTJlNFwvZGViOXJoZi1hMjhkYjJmMi0yNjNiLTQ1YjItOWJiZC1hNzg5NGNkNmUxMzMucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.M-DaJ89bFpvEZNmxSDH0XxSDGXvGd_79gUIPWT45kLU', tamanho = 75)

    with cr7_photo:
        st.subheader('C. Ronaldo')
        image_icones('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSsNcWjopG2OzaVnw3z8Nq0k9dXMMtMBkbtnQ&s')
        
    #mid2 será plotado a barra vertical
    # with mid2:
    #     st.html(
    #         '''
    #             <div class="divider-vertical-line"></div>
    #             <style>
    #                 .divider-vertical-line {
    #                     border-left: 2px solid rgba(49, 51, 63, 0.2);
    #                     height: 320px;
    #                     margin: auto;
    #                 }
    #             </style>
    #         '''
    #     )

    with mid:
        st.subheader('Barcelona')
        image_icones('https://upload.wikimedia.org/wikipedia/pt/thumb/4/43/FCBarcelona.svg/2020px-FCBarcelona.svg.png',tamanho= 120)
    
    with mid2:
        st.subheader('M. United')
        image_icones('https://upload.wikimedia.org/wikinews/en/thumb/7/7d/Manchester_United_F.C._logo.svg/1200px-Manchester_United_F.C._logo.svg.png', tamanho= 120)
        


    pitch_event = st.radio('Selecione a informação que deseja visualizar:',['Passes','Chutes'])

    def plot_event(event, match, player_name) -> None:
        if event == 'Passes':
            plot_passes(match=match, player_name=player_name)
        elif event == 'Chutes':
            plot_shot(match=match, player_name=player_name)

    messi_c, cr7_c = st.columns(2)

    with messi_c:
        st.write(f'{pitch_event} Realizados na Partida: ')
        fig_event_1 = plot_event(event = pitch_event, match=final_data,player_name=messi_name)
        st.pyplot(fig_event_1)
        analise_participacoes_messi = '''
        Através das participações no campo mostradas acima, é notável o quão o futuro melhor do mundo daquele ano, comandava o jogo e articulava sua equipe.
        Messi joga naturalmente na posição de ponta direita, porém através do campo não conseguimos identificar facilmente pois ele moveu-se sob todo o campo de defesa adversário.
        As suas finalizações foram abaixo do comum, porém mesmo assim fez o gol aos 70 minutos de jogo, que viria a definir a vitória pro time catalão.
        '''
        align_text(analise_participacoes_messi,'h6')

    with cr7_c:
        st.write(f'{pitch_event} Realizados na Partida: ')
        fig_event_2 = plot_event(event = pitch_event, match=final_data,player_name=cris_name)
        st.pyplot(fig_event_2)
        analise_participacoes_cr7 = '''
        Cristiano Ronaldo, então melhor jogador do mundo, não teve a final da Champions League 2009 como um jogo positivamente memorável.
        A análise de sua função tática no jogo foi razoavelmente boa, sendo um ponta esquerda e finalizando diversas vezes por esse lado do campo, em gol.
        Porém, essas chances não foram convertidas, mérito também do goleiro Victor Valdes que foi sublime em segurar o poderoso ataque dos Red Devil's.
        Como ja era de se esperar, a entrega para o time não foi um destaque de Cristiano Ronaldo, percepitível pelas poucos participações com passes durante o jogo. O time jogava para ele, e não o contrário.
        '''
        align_text(analise_participacoes_cr7)