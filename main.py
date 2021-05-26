# -*- coding: utf-8 -*-
from fastapi import FastAPI
from routers import uuid_generator

import models
from utils import database

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

app.include_router(uuid_generator.router)
