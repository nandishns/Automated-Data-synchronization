# src/services/firebase_listener.py
from firebase_admin import firestore
from src.services.google_sheets_service import google_sheets_service
import logging

class FirebaseListener:
    def __init__(self):
        self.db = firestore.client()
        self.collection_ref = self.db.collection('SalesData')

    def on_snapshot(self, col_snapshot, changes, read_time):
        for change in changes:
            if change.type.name == 'ADDED':
                print(f'New document: {change.document.id}')
                self.update_google_sheet(change.document.to_dict())
            elif change.type.name == 'MODIFIED':
                print(f'Modified document: {change.document.id}')
                self.update_google_sheet(change.document.to_dict())
            elif change.type.name == 'REMOVED':
                print(f'Removed document: {change.document.id}')
                # Handle document deletion in Google Sheets if needed

    def update_google_sheet(self, document_data):
        # Find the row in Google Sheets using the Product ID
        sheet_data = google_sheets_service.get_data()
        print(sheet_data)
        product_id = document_data.get('Product ID')

        # Find the row index by matching the Product ID
        row_index = next((index for (index, d) in enumerate(sheet_data, start=2) if d.get('Product ID') == product_id), None)

        if row_index:
            # Update the row in Google Sheets
            google_sheets_service.update_row(row_index, document_data)
            print(f"Updated row {row_index} in Google Sheets.")
        else:
            print(f"Product ID {product_id} not found in Google Sheets. Adding a new row.")
            # Optionally add a new row if not found
            google_sheets_service.append_row(document_data)

    def start_listening(self):
        # Listen to changes in the collection
        self.collection_ref.on_snapshot(self.on_snapshot)

# Start the Firebase listener
firebase_listener = FirebaseListener()
firebase_listener.start_listening()
