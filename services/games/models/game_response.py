from pydantic import BaseModel, Field


class GameResponse(BaseModel):
    category_uuids: list
    price: int = Field(..., ge=0)
    title: str
    uuid: str
