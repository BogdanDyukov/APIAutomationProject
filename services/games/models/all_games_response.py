from typing import List

from pydantic import BaseModel, Field

from services.games.models.game_response import GameResponse


class Meta(BaseModel):
    total: int = Field(..., ge=0)


class AllGamesResponse(BaseModel):
    meta: Meta
    games: List[GameResponse]
