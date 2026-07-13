import json
import logging
import time
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request

from app.config import get_settings

settings = get_settings()
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger("pipeline-demo")


def log_event(event: str, **fields: object) -> None:
    logger.info(json.dumps({"event": event, **fields}, separators=(",", ":")))


@asynccontextmanager
async def lifespan(_: FastAPI):
    log_event("application_started", version=settings.version)
    yield
    log_event("application_stopped")


app = FastAPI(title="Pipeline Demo API", version=settings.version, lifespan=lifespan)


@app.middleware("http")
async def request_log(request: Request, call_next):
    started = time.perf_counter()
    response = await call_next(request)
    log_event(
        "request_completed",
        method=request.method,
        path=request.url.path,
        status=response.status_code,
        duration_ms=round((time.perf_counter() - started) * 1000, 2),
    )
    return response


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "healthy", "version": settings.version}


@app.get("/api/info")
def info() -> dict[str, str]:
    return {
        "environment": settings.environment,
        "message": settings.greeting,
        "version": settings.version,
    }
