# -*- coding: utf-8 -*-
from fastapi import FastAPI

import models
from utils import database

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)
