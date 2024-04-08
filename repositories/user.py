import uuid

from sqlalchemy.orm import Session

from domain.models.user import User


def get_user(user_id: uuid, db: Session, ):
    return db.query(User).filter(User.user_id == user_id).first()


def get_users(db: Session, ):
    return db.query(User).all()


def delete_user(user_id: uuid, db: Session, ):
    user = get_user(user_id, db)
    db.delete(user)
    db.commit()
    message = f"user_id: {user_id} has been deleted successfully."
    return message

def create_user(user: User, db: Session, ):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_email(email, db: Session):
    return db.query(User).filter(User.user_mail == email).first()
