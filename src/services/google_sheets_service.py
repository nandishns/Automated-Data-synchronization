# app/services/google_sheets_service.py
import gspread
from src.config import settings

class GoogleSheetsService:
    def __init__(self):
        self.client = gspread.service_account(filename=settings.google_sheets_key)
        self.sheet = self.client.open(settings.sheet_name).sheet1

    def get_data(self):
        return self.sheet.get_all_records()

google_sheets_service = GoogleSheetsService()
