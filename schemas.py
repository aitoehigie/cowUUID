# -*- coding: utf-8 -*-
from datetime import datetime
from uuid import UUID
from typing import List

from pydantic import BaseModel


class BaseUUID(BaseModel):
    uuid: str


class CreateUUID(BaseUUID):
    pass


class ListUUID(BaseUUID):
    class Config:
        orm_mode = True
