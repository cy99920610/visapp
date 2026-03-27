from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.api import audit, communications, crm, knowledge
from app.core.db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="VIS-Recruit OS", version="1.0.0")
app.include_router(crm.router)
app.include_router(knowledge.router)
app.include_router(communications.router)
app.include_router(audit.router)

static_path = Path(__file__).parent / "static"
app.mount("/static", StaticFiles(directory=static_path), name="static")


@app.get("/")
def home():
    return FileResponse(static_path / "index.html")
