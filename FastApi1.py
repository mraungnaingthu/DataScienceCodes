from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()

@app.get("/root/lib/{id}")
async def history(
    id: int,
    date: Optional[str] = Query(None, description="Optional date to filter history")
):
    """
    Retrieves the history for a given ID.
    Optionally filters the history by a specific date.
    """
    response_message = f"This is history for id {id}"

    if date:
        response_message += f" and filtered by date: {date}"

    return {"message": response_message}
