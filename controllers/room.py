from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from config.database import get_session
from domain.schemas.room import RoomIn, Room

from services import room as room_service

router = APIRouter()

ROOM_TAG = "Room"


@router.post("/room", summary="Add new room", tags=[ROOM_TAG], response_model=Room)
def create_room(room: RoomIn, db: Session = Depends(get_session)):
    return room_service.create_room(room, db)


@router.get("/room", summary="Get all rooms", tags=[ROOM_TAG], response_model=list[Room])
def get_rooms(db: Session = Depends(get_session)):
    return room_service.get_rooms(db)
