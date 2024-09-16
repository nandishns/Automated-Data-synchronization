from firebase_admin import firestore
from src.services.google_sheets_service import google_sheets_service
from datetime import datetime
class FirebaseListener:
    def __init__(self):
        self.db = firestore.client()
        self.collection_ref = self.db.collection('SalesData')

    def on_snapshot(self, col_snapshot, changes, read_time):

        for change in changes:
            if change.type.name == 'ADDED':
                self.update_google_sheet(change.document.to_dict())
            elif change.type.name == 'MODIFIED':
                self.update_google_sheet(change.document.to_dict())
            elif change.type.name == 'REMOVED':
                self.remove_row_in_google_sheet(change.document.to_dict())

    @staticmethod
    def update_google_sheet(document_data):
        sheet_data = google_sheets_service.get_data()

        try:
            product_id = int(document_data.get('Product ID'))
        except (ValueError, TypeError):
            return

        firestore_timestamp = document_data.get('last_modified') or datetime.utcnow().isoformat()

        row_index = next(
            (index for (index, d) in enumerate(sheet_data, start=2) if int(d.get('Product ID', '')) == product_id),
            None
        )

        if row_index:
            sheet_timestamp = sheet_data[row_index - 2].get('last_modified',datetime.utcnow().isoformat())
            if firestore_timestamp > sheet_timestamp:
                google_sheets_service.update_row(row_index, document_data)
        else:
            google_sheets_service.append_row(document_data)

    @staticmethod
    def remove_row_in_google_sheet(document_data):
        sheet_data = google_sheets_service.get_data()

        try:
            product_id = int(document_data.get('Product ID'))
        except (ValueError, TypeError):
            return

        row_index = next(
            (index for (index, d) in enumerate(sheet_data, start=2) if int(d.get('Product ID', '')) == product_id),
            None
        )

        if row_index:
            google_sheets_service.delete_row(row_index)

    def start_listening(self):
        self.collection_ref.on_snapshot(self.on_snapshot)

firebase_listener = FirebaseListener()
firebase_listener.start_listening()
