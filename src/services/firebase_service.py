# app/services/firebase_service.py
from src.models.firebase import firebase_model

class FirebaseService:
    def update_data(self, data):
        firebase_model.update_firestore(data)

firebase_service = FirebaseService()
