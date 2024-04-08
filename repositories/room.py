import uuid
from sqlalchemy.orm import Session
from domain.models.model import Room


def get_room(room_id: uuid, db: Session):
    return db.query(Room).filter(Room.room_id == room_id).first()


def create_room(db_room, db: Session):
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room
