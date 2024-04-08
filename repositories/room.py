import uuid
from sqlalchemy.orm import Session
from domain.models.room import Room


def get_room(room_id: uuid, db: Session):
    return db.query(Room).filter(Room.room_id == room_id).first()


def get_rooms(db: Session):
    return db.query(Room).all()


def delete_room(room_id: uuid, db: Session):
    room = get_room(room_id, db)
    db.delete(room)
    db.commit()
    message = f"room_id: {room_id} has been deleted successfully."
    return message


def create_room(db_room, db: Session):
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room
