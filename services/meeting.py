from datetime import date, timedelta
from domain.models.model import Meeting
from domain.schemas.meeting import MeetingIn
from repositories import meeting as meeting_repository
from .user import get_user, get_users_by_id
from .room import get_room
from sqlalchemy.orm import Session
from fastapi import HTTPException


def create_meeting(meeting: MeetingIn, db: Session):
    list_users = []
    for user_uuid in meeting.participants:
        user = get_user(user_uuid, db)
        list_users.append(user)

    room = get_room(meeting.room_id, db)

    # validate if the room is available at the time
    meetings = meeting_repository.get_meetings(db)
    check_room_availableness(meeting, meetings, room)

    # validade if the user is available at the time
    user_check_availableness(list_users, meeting, meetings)

    meeting = Meeting(
        title=meeting.title,
        start_hour=meeting.start_hour,
        end_hour=meeting.end_hour,
        created_at=date.today(),
        participants=list_users,
        room_id=room.room_id
    )
    return meeting_repository.create_meeting(meeting, db)


def user_check_availableness(list_users, meeting, meetings):
    for user in list_users:
        for meet in meetings:
            if user in meet.participants:
                if meet.start_hour <= meeting.start_hour <= meet.end_hour or meet.start_hour <= meeting.end_hour <= meet.end_hour:
                    raise HTTPException(status_code=400, detail="User not available at the time")


def check_room_availableness(meeting, meetings, room):
    for meet in meetings:
        if meet.room_id == room.room_id:
            if meet.start_hour <= meeting.start_hour <= meet.end_hour or meet.start_hour <= meeting.end_hour <= meet.end_hour:
                raise HTTPException(status_code=400, detail="Room not available at the time")


def get_meeting(meeting_id, db):
    return meeting_repository.get_meeting(meeting_id, db)


def get_meetings(db):
    return meeting_repository.get_meetings(db)


def delete_meeting(meeting_id, db):
    meet = meeting_repository.get_meeting(meeting_id, db)
    if meet is None:
        return "Meeting not found"
    return meeting_repository.delete_meeting(meeting_id, db)


def add_participants(meeting_id, participants, db):
    meeting = get_meeting(meeting_id, db)
    list_users = get_users_by_id(participants, db)

    # add users who not in the meeting
    for user in list_users:
        if user not in meeting.participants:
            meeting.participants.append(user)

    # check if the user is available at the time
    user_check_availableness(list_users, meeting, get_meetings(db))

    return meeting_repository.add_participants(meeting, db)
