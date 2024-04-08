from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import get_session
from domain.schemas.room import RoomIn, Room, RoomOut
from uuid import UUID
from services import room as room_service

router = APIRouter()

ROOM_TAG = "Room"


@router.post("/room", summary="Add new room", tags=[ROOM_TAG], response_model=RoomOut)
def create_room(room: RoomIn, db: Session = Depends(get_session)):
    return room_service.create_room(room, db)


@router.get("/room", summary="Get all rooms", tags=[ROOM_TAG], response_model=list[RoomOut])
def get_rooms(db: Session = Depends(get_session)):
    return room_service.get_rooms(db)


@router.get("/room/{room_id}", summary="Get room by id", tags=[ROOM_TAG], response_model=RoomOut)
def get_room(room_id: UUID, db: Session = Depends(get_session)):
    return room_service.get_room(room_id, db)


@router.delete("/room/{room_id}", summary="Delete room by id", tags=[ROOM_TAG], response_model=str)
def delete_room(room_id: UUID, db: Session = Depends(get_session)):
    return room_service.delete_room(room_id, db)
