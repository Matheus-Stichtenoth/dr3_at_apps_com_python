from pydantic import BaseModel, Field

class MatchInput(BaseModel):
    match_id: int = Field(..., gt=0, description="O ID da partida deve ser um número inteiro positivo.")