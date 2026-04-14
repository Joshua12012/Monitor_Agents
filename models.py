from sqlalchemy import Column, String, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID
from database import Base
from pydantic import BaseModel
import uuid, datetime

class Agent(Base):
    __tablename__ = "agents"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    status = Column(String, default="stopped")
    status_log = Column(Text, default="")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class AgentCreate(BaseModel):
    name: str
    type: str

class StatusUpdate(BaseModel):
    status: str

