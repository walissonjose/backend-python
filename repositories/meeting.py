import uuid
from sqlalchemy.orm import Session
from domain.models.model import Meeting


def create_meeting(meeting: Meeting, db: Session):
    db.add(meeting)
    db.commit()
    db.refresh(meeting)
    return meeting
