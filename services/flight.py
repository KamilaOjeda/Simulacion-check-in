# from config.database import Database
# from schemas.flight import Flight
# from typing import List

# class FlightService:
#     def __init__(self, db: Database):
#         self.db = db
        
#     async def get_flights(self) -> List[Flight]:
#         flights = []
#         cursor = self.db.connection.cursor()
#         query = "SELECT * FROM flight"
#         cursor.execute(query)
#         return flights