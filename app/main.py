from fastapi import FastAPI, HTTPException
from football_stats.matches import get_match_events, summarize_events
from football_stats.players import get_player_profile
import json
import pandas as pd
from models.match_input import MatchInput
from models.player_input import PlayerInput

app = FastAPI()

@app.post("/match_summary")
def match_summary(input_data: MatchInput):
    try:
        # Obter eventos da partida
        events = get_match_events(input_data.match_id)
        if not events:
            raise HTTPException(status_code=404, detail="Nenhum evento encontrado para a partida.")
        
        # Resumo dos eventos
        summary = summarize_events(pd.DataFrame(json.loads(events)))
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao processar a solicitação: {str(e)}")

@app.post("/player_profile")
def player_profile(input_data: PlayerInput):
    try:
        # Obter perfil do jogador
        profile = get_player_profile(input_data.match_id, input_data.player_name)

        # Verificar se o perfil está vazio ou inválido
        if not profile or (isinstance(profile, dict) and all(value == 0 for value in profile.values())):
            raise HTTPException(
                status_code=404, 
                detail=f"O jogador '{input_data.player_name}' não foi encontrado na partida de ID {input_data.match_id}."
            )
        
        return profile
    except HTTPException as http_err:
        raise http_err
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Erro ao processar a solicitação: {str(e)}"
        )