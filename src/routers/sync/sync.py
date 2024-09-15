# src/routers/webhook.py
from fastapi import APIRouter, Request, logger


from src.services.google_sheets_service import google_sheets_service
from src.services.firebase_service import firebase_service

router = APIRouter()


@router.post("/sync")
async def sync_data(request: Request):
    change_data = await request.json()

    # Extract the row number from the change data
    row_number = change_data.get("row")

    if row_number is not None:
        try:

            sheet_data = google_sheets_service.get_data()

            # Adjusting the row number for 0-based index
            adjusted_index = row_number - 2

            if 0 <= adjusted_index < len(sheet_data):  # Correct bounds check
                row_data = sheet_data[adjusted_index]
                firebase_service.update_data([row_data])
                logger.logger.log("Firebase updated successfully.")
            else:

                return {"message": "Invalid row number"}
        except Exception as e:
            print(f"An error occurred: {e}")
            return {"message": "An error occurred while processing the request."}

    return {"message": "Data synchronized successfully"}
