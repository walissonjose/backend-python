from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from config.database import get_session
from domain.schemas.user import UserIn, User, UserOut

from services import user as user_service

router = APIRouter()

USER_TAG = "User"


@router.post("/users", summary="Add new user", tags=[USER_TAG], response_model=User)
def create_user(user: UserIn, db: Session = Depends(get_session)):
    return user_service.create_user(user, db)


@router.get("/users", summary="Get all users", tags=[USER_TAG], response_model=list[UserOut])
def get_users(db: Session = Depends(get_session)):
    return user_service.get_users(db)


@router.get("/users/{user_id}", summary="Get user by id", tags=[USER_TAG], response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_session)):
    return user_service.get_user(user_id, db)
