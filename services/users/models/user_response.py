from pydantic import BaseModel, field_validator


class UserResponse(BaseModel):
    email: str
    name: str
    nickname: str
    avatar_url: str
    uuid: str

    @field_validator("email", "name", "nickname", "uuid")
    def field_is_not_empty(cls, value):

        if not value or value is None:
            raise ValueError("Field is empty")

        return value
