import gspread
from src.config import settings
from datetime import datetime

class GoogleSheetsService:
    def __init__(self):
        self.client = gspread.service_account(filename=settings.google_sheet_key_path)
        self.sheet = self.client.open_by_key(settings.google_sheets_id).worksheet(settings.sheet_name)

    def get_data(self):
        return self.sheet.get_all_records()

    def update_row(self, row_index, data):
        last_modified = datetime.utcnow().isoformat()
        self.sheet.update(f'A{row_index}:H{row_index}', [[
            int(data.get('Product ID')) if data.get('Product ID') else '',
            data.get('Product'),
            data.get('Category'),
            data.get('Date'),
            int(data.get('Quantity Sold')) if data.get('Quantity Sold') else '',
            int(data.get('Unit Price')) if data.get('Unit Price') else '',
            int(data.get('Total Revenue')) if data.get('Total Revenue') else '',
            last_modified
        ]])

    def append_row(self, data):
        last_modified = datetime.utcnow().isoformat()
        self.sheet.append_row([
            int(data.get('Product ID')) if data.get('Product ID') else '',
            data.get('Product'),
            data.get('Category'),
            data.get('Date'),
            int(data.get('Quantity Sold')) if data.get('Quantity Sold') else '',
            int(data.get('Unit Price')) if data.get('Unit Price') else '',
            int(data.get('Total Revenue')) if data.get('Total Revenue') else '',
            last_modified
        ])

    def delete_row(self, row_index):
        self.sheet.delete_rows(row_index)


google_sheets_service = GoogleSheetsService()
