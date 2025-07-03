from typing import List

from pydantic import BaseModel, Field

from services.users.models.user_response import UserResponse


class Meta(BaseModel):
    total: int = Field(..., ge=0)


class AllUsersResponse(BaseModel):
    meta: Meta
    users: List[UserResponse]
