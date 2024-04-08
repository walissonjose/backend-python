import uuid

from sqlalchemy.orm import Session

from domain.models.model import User


def get_user(user_id: uuid, db: Session, ):
    return db.query(User).filter(User.user_id == user_id).first()


def get_users(db: Session, ):
    return db.query(User).all()


def create_user(user: User, db: Session, ):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_email(email, db: Session):
    return db.query(User).filter(User.user_mail == email).first()
