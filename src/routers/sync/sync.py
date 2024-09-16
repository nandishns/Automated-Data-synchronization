from fastapi import APIRouter, Request, HTTPException
from datetime import datetime

from src.services.google_sheets_service import google_sheets_service
from src.services.firebase_service import firebase_service

router = APIRouter()

@router.post("/sync")
async def sync_data(request: Request):
    try:
        change_data = await request.json()

        # Extract the row number from the change data
        row_number = change_data.get("row")

        if row_number is None:
            raise ValueError("Row number is not provided in the request data.")

        try:
            sheet_data = google_sheets_service.get_data()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error fetching data from Google Sheets: {e}")

        # Adjusting the row number for 0-based index
        adjusted_index = row_number - 2

        if 0 <= adjusted_index < len(sheet_data):  # Correct bounds check
            try:
                row_data = sheet_data[adjusted_index]
                row_data['last_modified'] = datetime.utcnow().isoformat()
                firebase_service.update_data([row_data])
                print(f"Row {row_number} synchronized successfully.")
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Error updating Firebase: {e}")
        else:
            raise ValueError("Invalid row number provided.")

    except ValueError as ve:
        print(f"Value Error: {ve}")
        return {"message": str(ve)}
    except HTTPException as http_exc:
        print(f"HTTP Exception: {http_exc.detail}")
        raise http_exc
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {e}")

    return {"message": "Data synchronized successfully"}
