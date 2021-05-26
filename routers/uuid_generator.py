# -*- coding: utf-8 -*-
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# import crud, models
import schemas
# from utils import database
from utils.db_utils import get_db

router = APIRouter(prefix="/api/v1", tags=["UUID Generator"])


@router.get("/uuid/", response_model=List[schemas.ListUUID])
async def generate_uuid(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    pass
