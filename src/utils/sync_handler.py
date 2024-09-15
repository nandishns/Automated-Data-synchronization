# app/utils/sync_handler.py
from src.services.google_sheets_service import google_sheets_service
from src.services.firebase_service import firebase_service

class SyncHandler:
    def sync_data(self):
        # Fetch data from Google Sheets
        data = google_sheets_service.get_data()
        # Update Firebase with the fetched data
        firebase_service.update_data(data)

sync_handler = SyncHandler()
