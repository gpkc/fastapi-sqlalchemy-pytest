from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.config import config
from app.services.database import sessionmanager


def init_app(init_db=True):
    lifespan = None

    if init_db:
        sessionmanager.init(config.DB_CONFIG)

        @asynccontextmanager
        async def lifespan(app: FastAPI):
            yield
            if sessionmanager._engine is not None:
                await sessionmanager.close()

    server = FastAPI(title="FastAPI server", lifespan=lifespan)

    from app.views.user import router as user_router

    server.include_router(user_router, prefix="/api", tags=["user"])

    return server
