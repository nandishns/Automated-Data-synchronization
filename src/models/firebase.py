# app/models/firebase.py
import firebase_admin
from firebase_admin import credentials, firestore
from src.config import settings

class FirebaseModel:
    def __init__(self):
        cred = credentials.Certificate(settings.firebase_credentials)
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def update_firestore(self, data):
        # Assuming a collection named 'excelData'
        collection_ref = self.db.collection('excelData')
        for record in data:
            collection_ref.document(record['id']).set(record)

firebase_model = FirebaseModel()
