# app/config.py
from pydantic_settings import BaseSettings
from pydantic import Field
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings(BaseSettings):
    firebase_credentials: str = Field(..., alias='FIREBASE_ADMIN_KEY_PATH')
    google_sheet_key_path: str = Field(..., alias='GOOGLE_SHEETS_KEY_PATH')
    google_sheets_id: str = Field(..., alias='GOOGLE_SHEETS_ID')
    sheet_name: str = Field(..., alias='GOOGLE_SHEET_NAME')

    class Config:
        env_file = ".env"
        extra = 'forbid'

settings = Settings()
