from fastapi import APIRouter
from config.database import Database
from schemas.flight import Flight
from typing import List

flight_router = APIRouter()

@flight_router.get("/flight", response_model=List[Flight])
def get_flights():
    db = Database()
    connection_method = db.connection
    connection_method()
    result = db.get_flights()
    db.disconnect()
    return result