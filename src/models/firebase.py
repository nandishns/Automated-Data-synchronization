import firebase_admin
from firebase_admin import credentials, firestore
from src.config import settings
from datetime import datetime

class FirebaseModel:
    def __init__(self):
        cred = credentials.Certificate(settings.firebase_credentials)
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()
        self.collection_ref = self.db.collection('SalesData')

    def update_firestore(self, data):
        # Assuming a collection named 'SalesData'
        collection_ref = self.db.collection('SalesData')

        for record in data:
            # Constructing the document data based on the new schema
            document_data = {
                'Product ID': int(record.get('Product ID')),
                'Product': record.get('Product'),
                'Category': record.get('Category'),
                'Date': record.get('Date'),
                'Quantity Sold': record.get('Quantity Sold'),
                'Unit Price': record.get('Unit Price'),
                'Total Revenue': record.get('Total Revenue'),
                'last_modified': datetime.utcnow().isoformat()
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

    def delete_document_by_product_id(self, product_id):
        try:
            self.collection_ref.document(str(product_id)).delete()
            print(f"Deleted document with Product ID {product_id}")
        except Exception as e:
            print(f"An error occurred while deleting document with Product ID {product_id}: {e}")



firebase_model = FirebaseModel()
