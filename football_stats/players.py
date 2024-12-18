import json
from statsbombpy import sb

def get_player_profile(match_id: int, player_name: str):
    """
    Retorna o perfil do jogador ou uma mensagem indicando que ele não foi encontrado.
    """
    try:
        # Carregar eventos da partida
        events = sb.events(match_id=match_id)

        # Filtrar eventos do jogador
        player_events = events[events["player"] == player_name]

        if player_events.empty:
            return None  # Indica que o jogador não foi encontrado

        # Verificar se as colunas necessárias estão presentes
        columns = events.columns
        profile = {}

        if "type" in columns and "outcome" in columns:
            profile["passes_completed"] = len(player_events[(player_events["type"] == "Pass") & (player_events["outcome"] == "Complete")])
            profile["shots_on_target"] = len(player_events[(player_events["type"] == "Shot") & (player_events["outcome"] == "On Target")])
            profile["goals"] = len(player_events[(player_events["type"] == "Shot") & (player_events["outcome"] == "Goal")])
        else:
            profile["passes_completed"] = len(player_events[player_events["type"] == "Pass"]) if "type" in columns else 0
            profile["shots_on_target"] = len(player_events[player_events["type"] == "Shot"]) if "type" in columns else 0
            profile["goals"] = 0  # Não pode calcular gols sem a coluna outcome

        # Outras estatísticas podem ser adicionadas aqui...
        return profile
    except Exception as e:
        raise ValueError(f"Erro ao buscar perfil do jogador: {str(e)}")