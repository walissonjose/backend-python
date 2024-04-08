import uuid

from fastapi import HTTPException
from sqlalchemy.orm import Session

from domain.schemas.room import RoomIn as roomIn
from domain.models.model import Room as roomModel
from repositories import room as room_repository


def create_room(room: roomIn, db: Session):
    db_room = roomModel(room_name=room.room_name, room_capacity=room.room_capacity)
    return room_repository.create_room(db_room, db)


def get_room(room_id: uuid, db: Session):
    room = room_repository.get_room(room_id, db)
    if room is None:
        raise HTTPException(status_code=404, detail="Room not found")
    return room


def get_rooms(db: Session):
    return room_repository.get_rooms(db)


def delete_room(room_id: uuid, db: Session):
    room = room_repository.get_room(room_id, db)
    if room is None:
        raise HTTPException(status_code=404, detail="Room not found")

    return room_repository.delete_room(room_id, db)
