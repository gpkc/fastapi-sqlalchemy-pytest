import os


class Config:
    DB_CONFIG = os.getenv(
        "DB_CONFIG",
        "postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}".format(
            DB_USER=os.getenv("DB_USER", "fastapi"),
            DB_PASSWORD=os.getenv("DB_PASSWORD", "fastapi-password"),
            DB_HOST=os.getenv("DB_HOST", "fastapi-postgresql:5432"),
            DB_NAME=os.getenv("DB_NAME", "fastapi"),
        ),
    )


config = Config
