from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from .generic import metadata


participants_association = Table(
    'participants', metadata,
    Column('meet_cd_meeting', UUID, ForeignKey('calendar.meetings.meet_cd_meeting'), primary_key=True),
    Column('user_cd_participant', UUID, ForeignKey('calendar.users.user_cd_user'), primary_key=True)
)
