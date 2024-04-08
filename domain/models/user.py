from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid
from .generic import GenericModel
from .participants import participants_association


class User(GenericModel):
    __tablename__ = "users"
    user_id: UUID = Column('user_cd_user', UUID, primary_key=True, unique=True, default=uuid.uuid4, nullable=False)
    user_name: str = Column('user_nm_user', String, nullable=False)
    user_mail: str = Column('user_nm_mail', String, nullable=False)
    meetings = relationship("Meeting", secondary=participants_association, back_populates="participants")
