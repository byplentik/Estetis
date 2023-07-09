import uuid

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID

Base = declarative_base()


class Task(Base):
    __tablename__ = 'tasks'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    task_uuid = sa.Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    description = sa.Column(sa.String, nullable=False)
    params = sa.Column(sa.JSON, nullable=False)
