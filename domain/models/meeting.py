from datetime import date, datetime
import uuid
from sqlalchemy import Column, Date, DateTime, ForeignKey, String, Table
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from .generic import GenericModel
from .participants import participants_association


class Meeting(GenericModel):
    __tablename__ = "meetings"
    meet_id: UUID = Column('meet_cd_meeting', UUID, primary_key=True, unique=True, default=uuid.uuid4)
    title: str = Column('meet_nm_title', String, nullable=False)
    start_hour = Column('meet_df_start', DateTime, nullable=False)
    end_hour = Column('meet_df_end', DateTime, nullable=False)
    created_at: date = Column('meet_dt_created', Date, nullable=False)

    participants = relationship("User", secondary=participants_association, back_populates="meetings")

    room_id = Column('room_cd_room', UUID, ForeignKey('calendar.rooms.room_cd_room'), nullable=False)
    room = relationship("Room", back_populates="meetings")
