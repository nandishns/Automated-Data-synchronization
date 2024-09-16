import logging

from src.models.firebase import firebase_model


class FirebaseService:

    @staticmethod
    def update_data(data):
        logging.info("Updating Firestore with data: %s", data)
        firebase_model.update_firestore(data)

    @staticmethod
    def delete_document_by_product_id(product_id):
        # Query to find the document with the given Product ID
        firebase_model.delete_document_by_product_id(product_id)


firebase_service = FirebaseService()
