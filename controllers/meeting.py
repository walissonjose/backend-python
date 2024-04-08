from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from config.database import get_session
from domain.schemas.meeting import MeetingIn, MeetingOut
from services import meeting as meeting_service
from uuid import UUID

router = APIRouter()

MEETING_TAG = "Meeting"


@router.post("/meeting", summary="Add new meeting", tags=[MEETING_TAG], response_model=MeetingOut)
def create_meeting(meeting: MeetingIn, db: Session = Depends(get_session)):
    return meeting_service.create_meeting(meeting, db)


@router.get(
    "/meeting/{meeting_id}",
    summary="Get meeting by id",
    tags=[MEETING_TAG],
    response_model=MeetingOut
)
def get_meeting(meeting_id: UUID, db: Session = Depends(get_session)):
    return meeting_service.get_meeting(meeting_id, db)


@router.get(
    "/meetings",
    summary="Get all meetings",
    tags=[MEETING_TAG],
    response_model=list[MeetingOut]
)
def get_meetings(db: Session = Depends(get_session)):
    return meeting_service.get_meetings(db)


@router.delete(
    "/meeting/{meeting_id}",
    summary="Delete meeting by id",
    tags=[MEETING_TAG],
    response_model=str
)
def delete_meeting(meeting_id: UUID, db: Session = Depends(get_session)):
    return meeting_service.delete_meeting(meeting_id, db)


@router.put(
    "/meeting/{meeting_id}",
    summary="Add new participant to meeting",
    tags=[MEETING_TAG],
    response_model=MeetingOut
)
def add_participants(meeting_id: UUID, participants: list[UUID], db: Session = Depends(get_session)):
    return meeting_service.add_participants(meeting_id, participants, db)