from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData(schema="calendar")
Base = declarative_base(metadata=metadata)

class GenericModel(Base):
    __abstract__ = True
