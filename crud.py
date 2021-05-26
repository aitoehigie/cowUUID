# -*- coding: utf-8 -*-
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

import models
import schemas


def create_uuid(db: Session, uuid: schemas.CreateUUID):
    db_uuid = models.UUID(uuid=uuid.uuid)
    db.add(db_uuid)
    db.commit()
    db.refresh(db_uuid)
    return db_uuid


def read_uuids(db: Session, skip: int = 0, limit: int = 100):
    db_uuid = db.query(models.UUID).order_by(
        models.UUID.id.desc()).offset(skip).limit(limit).all()
    if not db_uuid:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="No UUID's found!"
        )
    return db_uuid
