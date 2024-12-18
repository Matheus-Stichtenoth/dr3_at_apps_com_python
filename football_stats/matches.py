import json
import pandas as pd
from statsbombpy import sb

def get_match_events(match_id: int) -> str:
    """
    Retorna os eventos de uma partida no formato JSON.
    """
    events = sb.events(match_id=match_id)
    return json.dumps(events.to_dict(orient='records'))


def summarize_events(events_df: pd.DataFrame) -> str:
    """
    Sumariza eventos principais como gols, assistências e cartões.
    """
    goals = events_df[events_df['type'] == 'Shot']
    cards = events_df[events_df['type'] == 'Card']

    summary = []
    for _, goal in goals.iterrows():
        if goal['shot_outcome'] == 'Goal':
            summary.append(f"GOL! {goal['player']} marcou aos {goal['minute']} minutos.")

    for _, card in cards.iterrows():
        summary.append(f"Cartão {card['card_type']} para {card['player']} aos {card['minute']} minutos.")

    return " ".join(summary)

def get_match_name(match_id: int) -> str:
    """
    Retorna o nome da partida, que será composta pelo campeonato, 
    e as duas equipes participantes.
    """
    sb.matches['']