from fastapi import FastAPI
from sqlmodel import SQLModel

from utils.db_session import engine
from utils.qbit_client import qbit_client

from users.router import router as users_router
from playback_sessions.router import router as playback_sessions_router


app = FastAPI()

qbit_client.login()
SQLModel.metadata.create_all(engine)

app.include_router(users_router, prefix="/users", tags=["users"])
app.include_router(
    playback_sessions_router, prefix="/playback_sessions", tags=["playback_sessions"]
)
