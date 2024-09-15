# app/services/firebase_service.py
import logging

from src.models.firebase import firebase_model

class FirebaseService:
    def update_data(self, data):
        logging.info("Updating Firestore with data: %s", data)
        firebase_model.update_firestore(data)

firebase_service = FirebaseService()
