from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from config.database import Database
from schemas.flight import Flight
from typing import List
from services.flight import FlightService

flight_router = APIRouter()

@flight_router.get("/flight", tags=["flights"], status_code=200)
async def get_flights() -> List[Flight]:
    db = Database
    service = await FlightService(db)
    result = service.get_flights()
    return result