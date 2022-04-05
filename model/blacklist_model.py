from sqlalchemy.sql import func
from sqlalchemy import Column, Text, String, DateTime, Float, Integer, DateTime
from .base import Base
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

class Blacklist(Base):
    __tablename__ = "blacklist"
    
    id = Column(Integer, primary_key=True)    
    email = Column(String(256))
    app_uuid = Column(String(256))
    blocked_reason = Column(String(256))
    ip_address = Column(String(256))
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

pydantic_parser = sqlalchemy_to_pydantic(Blacklist)

def convertToList(lsBlacklist):
    return list(map(convertItem, lsBlacklist))

def convertItem(objBlacklist):
    return pydantic_parser.from_orm(objBlacklist).dict()