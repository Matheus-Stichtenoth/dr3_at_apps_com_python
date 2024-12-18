from pydantic import BaseModel, Field

class PlayerInput(BaseModel):
    match_id: int = Field(..., gt=0, description="O ID da partida deve ser um número inteiro positivo.")
    player_name: str = Field(..., min_length=1, max_length=100, description="O nome do jogador deve ter entre 1 e 100 caracteres.")