import logging
import sys

from fastapi import FastAPI, logger
from fastapi.middleware.cors import CORSMiddleware
from src.routers.sync.sync import router as SYNC
from src.routers.delete_row.delete_row import router as DELETE_ROW
from .services.firebase_listener_service import firebase_listener

from .utils.utils import read_markdown_file

readme_content = read_markdown_file("READMe.md")

logging.basicConfig(stream=sys.stdout,
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = FastAPI(
    title="SuperJoin Assignment",
    description=(lambda: readme_content
    if isinstance(readme_content, str) else "")(),
    version="1.0.0",
)

@app.on_event("startup")
async def startup_event():
    firebase_listener.start_listening()
    print("Firebase listener started.")

app.include_router(SYNC, tags=["SuperJoin Assignment"])
app.include_router(DELETE_ROW, tags=["SuperJoin Assignment"])


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
