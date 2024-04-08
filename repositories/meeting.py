import uuid
from sqlalchemy.orm import Session
from domain.models.model import Meeting


def create_meeting(meeting: Meeting, db: Session):
    db.add(meeting)
    db.commit()
    db.refresh(meeting)
    return meeting


def get_meeting(meeting_id: uuid, db: Session):
    return db.query(Meeting).filter(Meeting.meet_id == meeting_id).first()


