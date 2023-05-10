from pydantic import BaseModel

class Flight(BaseModel):
    flight_id: int
    takeoff_date_time: int
    takeoff_airport: str
    landing_date_time: int
    landing_airport: str
    airplane_id: int