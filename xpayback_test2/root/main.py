from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from models import models
from database.database import engine
from routers import user


app = FastAPI(title='xpayback_task2')

models.Base.metadata.create_all(engine)
app.mount("/media", StaticFiles(directory="media"), name="media")

app.include_router(user.router)
