# -*- coding: utf-8 -*-
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func

from utils.database import Base


class UUID(Base):
    __tablename__ = "uuids"
    id = Column(name="id", type_=Integer, primary_key=True, unique=True, index=True)
    uuid = Column(name="uuid", type_=String, index=True)
    timestamp = Column(
        name="timestamp", type_=DateTime(timezone=True), server_default=func.now()
    )
