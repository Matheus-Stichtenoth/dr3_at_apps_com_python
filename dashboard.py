import streamlit as st
from src.page_dashboard import func_dashboard
from src.page_narracao import func_narracao
from src.page_question import func_question
from src.page_jogadores import func_jogador


menu_lateral = [
    'Home 🏠',
    'Dashboard Campeonato/Partida 🏆',
    'Narração de Partida 🗣',
    'Dúvidas Sobre Partida ⁉',
    'Comparativos Jogadores 🆚'
]

st.title('Central do Pós-Jogo!')

def dashboard() -> None:
    choice = st.sidebar.selectbox('Páginas', menu_lateral)
    if choice == 'Dashboard Campeonato/Partida 🏆':
        func_dashboard()
    elif choice == 'Narração de Partida 🗣':
        func_narracao()
    elif choice == 'Home 🏠':
        st.image('https://static.vecteezy.com/system/resources/previews/021/629/525/non_2x/icon-a-football-player-kicking-a-ball-free-png.png')
    elif choice == 'Dúvidas Sobre Partida ⁉':
        func_question()
    elif choice == 'Comparativos Jogadores 🆚':
        func_jogador()

if __name__ == '__main__':
    dashboard()