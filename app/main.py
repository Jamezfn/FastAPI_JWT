from fastapi import FastAPI

from routers import auth, protected
from dB.base import Base
from dB.session import engine
import models

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(protected.router)

