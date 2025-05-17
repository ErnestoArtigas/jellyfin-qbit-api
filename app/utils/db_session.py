from contextlib import contextmanager
import traceback
from fastapi import HTTPException, status

from sqlmodel import Session, create_engine
from sqlalchemy import event
from sqlalchemy.orm import sessionmaker

from users.model import *  # noqa: F403
from playback_sessions.model import *  # noqa: F403


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url)

event.listen(engine, "connect", lambda c, _: c.execute("pragma foreign_keys=on"))

DBSession = sessionmaker(bind=engine, class_=Session)


@contextmanager
def get_session():
    session = DBSession()

    try:
        yield session
        session.commit()
    except Exception as err:
        print(traceback.format_exc())
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error, please read the logs. {err}",
        )
