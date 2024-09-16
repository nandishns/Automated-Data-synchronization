# src/routers/webhook.py
from fastapi import APIRouter, Request
from src.services.firebase_service import firebase_service

router = APIRouter()

@router.post("/delete_row")
async def delete_row(request: Request):
    try:
        data = await request.json()
        print("Delete received: ", data)
        product_id = data.get('productID')

        if product_id:
            firebase_service.delete_document_by_product_id(product_id)
            return {"message": f"Document with Product ID {product_id} deleted from Firebase."}

        return {"message": "Product ID not provided."}
    except Exception as e:
        return {"message": f"An error occurred while processing the request: {e}"}
