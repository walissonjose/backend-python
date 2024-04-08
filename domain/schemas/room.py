from uuid import UUID
from .generic import GenericModel
from pydantic import Field


class Room(GenericModel):
    room_name: str = Field(default="Room 1")


class RoomIn(Room):
    room_capacity: int = Field(default=10)


class RoomOut(RoomIn):
    room_id: UUID = Field(default=UUID)
