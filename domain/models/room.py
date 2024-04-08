from .generic import GenericModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Room(GenericModel):
    __tablename__ = "rooms"
    room_id: UUID = Column('room_cd_room', UUID, primary_key=True, unique=True, default=uuid.uuid4)
    room_name: str = Column('room_nm_room', String, nullable=False)
    room_capacity: int = Column('room_nr_capacity', Integer, nullable=False)
    meetings = relationship("Meeting", back_populates="room")
