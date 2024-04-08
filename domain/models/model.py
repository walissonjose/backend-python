import uuid

from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData, Column, Integer, String, ForeignKey, Table, DateTime, Date
from datetime import date

metadata = MetaData(schema="calendar")
Base = declarative_base(metadata=metadata)

participants_association = Table(
    'participants', metadata,
    Column('meet_cd_meeting', UUID, ForeignKey('calendar.meetings.meet_cd_meeting'), primary_key=True),
    Column('user_cd_participant', UUID, ForeignKey('calendar.users.user_cd_user'), primary_key=True)
)


class GenericModel(Base):
    __abstract__ = True


class User(GenericModel):
    __tablename__ = "users"
    user_id: UUID = Column('user_cd_user', UUID, primary_key=True, unique=True, default=uuid.uuid4, nullable=False)
    user_name: str = Column('user_nm_user', String, nullable=False)
    user_mail: str = Column('user_nm_mail', String, nullable=False)
    meetings = relationship("Meeting", secondary=participants_association, back_populates="participants")


class Room(GenericModel):
    __tablename__ = "rooms"
    room_id: UUID = Column('room_cd_room', UUID, primary_key=True, unique=True, default=uuid.uuid4)
    room_name: str = Column('room_nm_room', String, nullable=False)
    room_capacity: int = Column('room_nr_capacity', Integer, nullable=False)
    meetings = relationship("Meeting", back_populates="room")


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
