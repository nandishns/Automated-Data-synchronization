# app/models/firebase.py
import firebase_admin
from firebase_admin import credentials, firestore
from src.config import settings
import uuid  # Import the uuid module for generating unique IDs

class FirebaseModel:
    def __init__(self):
        cred = credentials.Certificate(settings.firebase_credentials)
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def update_firestore(self, data):
        # Assuming a collection named 'SalesData'
        collection_ref = self.db.collection('SalesData')

        for record in data:
            # Constructing the document data based on the new schema
            document_data = {
                'Product ID': record.get('Product ID'),
                'Product': record.get('Product'),
                'Category': record.get('Category'),
                'Date': record.get('Date'),
                'Quantity Sold': record.get('Quantity Sold'),
                'Unit Price': record.get('Unit Price'),
                'Total Revenue': record.get('Total Revenue')
            }

            # Check if all fields are empty
            if all(not value for value in document_data.values()):
                # Skip this record if all fields are empty
                continue

            document_id = str(record.get('Product ID'))
            document_data['Product ID'] = document_id

            # Check if the document already exists using the UUID
            existing_doc = collection_ref.document(document_id).get()

            if existing_doc.exists:
                # Document exists, update it
                collection_ref.document(document_id).set(document_data)
                print(f"Document {document_id} updated.")
            else:
                # Document doesn't exist, create a new one
                collection_ref.document(document_id).set(document_data)
                print(f"Document {document_id} created.")
                # Optionally: you can update the Google Sheet to store this UUID in the corresponding row

firebase_model = FirebaseModel()
