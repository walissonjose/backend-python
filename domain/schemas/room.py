from uuid import UUID
from .generic import GenericModel


class Room(GenericModel):
    room_id: UUID
    room_name: str

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "room_id": "123e4567-e89b-12d3-a456-426614174000",
                "room_name": "Room 1"
            }
        }


class RoomIn(Room):
    room_capacity: int

    class Config:
        json_schema_extra = {
            "example": {
                "room_id": "123e4567-e89b-12d3-a456-426614174000",
                "room_name": "Room 1",
                "room_capacity": 20
            }
        }
