# app/config.py
import os
from pydantic import Base

class Settings(Base):
    firebase_credentials: str = ""
    google_sheets_key: str = ""
    sheet_name: str = ""

    class Config:
        env_file = ".env"

settings = Settings()
