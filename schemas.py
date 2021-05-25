# -*- coding: utf-8 -*-
from datetime import datetime
from typing import List

from pydantic import BaseModel


class BaseUUID(BaseModel):
    uuid: str
    timestamp: datetime


class CreateUUID(BaseUUID):
    pass


class ListUUID(BaseUUID):
    class Config:
        orm_mode = True
