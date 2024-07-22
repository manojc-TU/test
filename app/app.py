import sentry_sdk
from fastapi import FastAPI

from app.constants import (
    ENVIRONMENT,
    SENTRY_DSN,
)
from app.database import Base, engine
from app.routers import chat, image, text, video

if SENTRY_DSN:
    sentry_sdk.init(dsn=SENTRY_DSN, environment=ENVIRONMENT, traces_sample_rate=0.25)

app = FastAPI()
Base.metadata.create_all(bind=engine)


app.include_router(chat.router)
app.include_router(image.router)
app.include_router(text.router)
app.include_router(video.router)
