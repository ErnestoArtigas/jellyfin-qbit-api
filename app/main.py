from contextlib import contextmanager
from typing import Any
from fastapi import Body, FastAPI
from sqlmodel import SQLModel

from playback_sessions.schema import PlaybackSessionPublic
from utils.qbit_client import qbit_client
from utils.db_session import engine

from users.router import router as users_router
from playback_sessions.router import router as playback_sessions_router


app = FastAPI()

SQLModel.metadata.create_all(engine)

app.include_router(users_router, prefix="/users", tags=["users"])
app.include_router(
    playback_sessions_router, prefix="/playback_sessions", tags=["playback_sessions"]
)


@app.get("/test")
def test():
    qbit_client.login()
    qbit_client.stop_torrents()
    return {"Test": "Working"}
