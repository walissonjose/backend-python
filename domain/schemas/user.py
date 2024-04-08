from uuid import UUID
from .generic import GenericModel
from pydantic import EmailStr


class User(GenericModel):
    user_name: str
    user_mail: EmailStr

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "name": "johndoe",
                "email": "johndoe@mail.com.br"
            }
        }


class UserIn(User):
    user_id: UUID

    class Config:
        json_schema_extra = {
            "example": {
                "user_id": "123e4567-e89b-12d3-a456-426614174000",
                "user_name": "johndoe",
                "user_mail": "johndoe@mail.com.br"
            }
        }
