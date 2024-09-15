# src/services/google_sheets_service.py
import gspread
from src.config import settings

class GoogleSheetsService:
    def __init__(self):
        self.client = gspread.service_account(filename=settings.google_sheet_key_path)
        self.sheet = self.client.open_by_key(settings.google_sheets_id).worksheet(settings.sheet_name)

    def get_data(self):
        # Fetch all data from the sheet
        return self.sheet.get_all_records()

    def update_row(self, row_index, data):
        self.sheet.update(f'A{row_index}:G{row_index}', [[
            data.get('Product ID'),
            data.get('Product'),
            data.get('Category'),
            data.get('Date'),
            data.get('Quantity Sold'),
            data.get('Unit Price'),
            data.get('Total Revenue'),
        ]])

    def append_row(self, data):
        self.sheet.append_row([
            data.get('Product ID'),
            data.get('Product'),
            data.get('Category'),
            data.get('Date'),
            data.get('Quantity Sold'),
            data.get('Unit Price'),
            data.get('Total Revenue'),
        ])

google_sheets_service = GoogleSheetsService()
