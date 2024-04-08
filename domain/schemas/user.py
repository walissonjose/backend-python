from uuid import UUID
from .generic import GenericModel
from pydantic import EmailStr, Field


class User(GenericModel):
    user_name: str = Field(default="John Doe")
    user_mail: EmailStr = Field(default="johndoe@mail.com")


class UserOut(User):
    user_id: UUID = Field(default=UUID)
