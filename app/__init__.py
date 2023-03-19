from fastapi import FastAPI

from app.config import config
from app.services.database import sessionmanager


def init_app(init_db=True):
    server = FastAPI(title="FastAPI server")

    if init_db:
        sessionmanager.init(config.DB_CONFIG)

        @server.on_event("shutdown")
        async def shutdown():
            await sessionmanager.close()

    from app.views.user import router as user_router

    server.include_router(user_router, prefix="/api", tags=["user"])

    return server
