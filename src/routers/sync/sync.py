# app/routers/sync.py
from fastapi import APIRouter
from src.utils.sync_handler import sync_handler

router = APIRouter()

@router.post("/sync")
async def sync_data():
    sync_handler.sync_data()
    return {"message": "Data synchronized successfully"}
