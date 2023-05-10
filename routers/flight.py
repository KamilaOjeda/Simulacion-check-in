from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
# from services.flight import TripService
# from schemas.flight import TripCreate, Trip

# from database.database import Database

# router = APIRouter()

# @router.get("/flight", response_model=List[Trip])
# async def get_flights(db: Database = Depends(), skip: int = 0, limit: int = 100):
#     trip_service = TripService(db)
#     flights = trip_service.get_flights(skip=skip, limit=limit)
#     return flights
