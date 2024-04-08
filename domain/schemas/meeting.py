from datetime import datetime, date, timedelta
from uuid import UUID
from pydantic import Field
from sqlalchemy import DateTime, Date
from .generic import GenericModel
from .user import User
from .room import Room


class Meeting(GenericModel):
    title: str = Field(default="Meeting")
    start_hour: datetime = Field(default=datetime.now())
    end_hour: datetime = Field(default=datetime.now() + timedelta(hours=2))
    created_at: date = Field(default=date.today())


class MeetingIn(Meeting):
    participants: list[UUID] = []
    room_id: UUID = Field(default=UUID)


class MeetingAddParticipants(GenericModel):
    meeting: UUID = Field(default=UUID)
    participant: list[UUID] = []


class MeetingOut(Meeting):
    meet_id: UUID = Field(default=UUID)
    participants: list[User] = []
    room: Room
