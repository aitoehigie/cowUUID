# -*- coding: utf-8 -*-
import uuid
from typing import List
import crud
import schemas

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import schemas
from utils.db_utils import get_db

router = APIRouter(prefix="/api/v1", tags=["UUID Generator"])


@router.get("/uuid/", response_model=List[schemas.ListUUID])
async def generate_uuid(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_uuid = schemas.CreateUUID(uuid=str(uuid.uuid4()))
    crud.create_uuid(db=db, uuid=db_uuid)
    result = crud.read_uuids(skip=0, limit=100, db=db)
    return result
