from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from config.database import get_session
from domain.schemas.user import UserIn, User

from services import user as user_service

router = APIRouter()

USER_TAG = "User"


@router.post("/users", summary="Add new user", tags=[USER_TAG], response_model=User)
def create_user(user: UserIn, db: Session = Depends(get_session)):
    return user_service.create_user(user, db)
