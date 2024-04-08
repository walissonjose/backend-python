from datetime import date, timedelta
from domain.models.model import Meeting
from domain.schemas.meeting import MeetingIn
from repositories import meeting as meeting_repository
from sqlalchemy.orm import Session
from .user import get_user


def create_meeting(meeting: MeetingIn, db: Session):
    list_users = []
    for user_uuid in meeting.participants:
        list_users.append(get_user(user_uuid, db))

    meeting = Meeting(
        title=meeting.title,
        start_hour=meeting.start_hour,
        end_hour=meeting.end_hour,
        created_at=date.today(),
        participants=list_users,
        room_id=meeting.room_id
    )
    return meeting_repository.create_meeting(meeting, db)


def add_participants(meeting, db):
    return None
