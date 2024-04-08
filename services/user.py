import uuid

from fastapi import HTTPException
from sqlalchemy.orm import Session

from domain.schemas.user import User as userCreate
from domain.models.model import User as userModel
from repositories import user as user_repository


def get_user(user_id: uuid, db: Session):
    user = user_repository.get_user(user_id, db)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def get_users(db: Session):
    return user_repository.get_users(db)


def delete_user(user_id: uuid, db: Session):
    user = get_user(user_id, db)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user_repository.delete_user(user_id, db)


def get_user_by_email(email, db: Session):
    return user_repository.get_user_by_email(email, db)


def create_user(user: userCreate, db: Session):
    db_user = get_user_by_email(user.user_mail, db)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    db_user = userModel(user_name=user.user_name, user_mail=user.user_mail)
    return user_repository.create_user(db_user, db)
