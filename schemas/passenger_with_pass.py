import json
from typing import Any

class PassengerWithBoardingPass:
    def __init__(self, passengerId, dni, name, age, country, boardingPassId, purchaseId, seatTypeId, seatId):
        self.passengerId = passengerId
        self.dni = dni
        self.name = name
        self.age = age
        self.country = country
        self.boardingPassId = boardingPassId
        self.purchaseId = purchaseId
        self.seatTypeId = seatTypeId
        self.seatId = seatId

class PassengerWithBoardingPassEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, PassengerWithBoardingPassEncoder):
            return o.__dict__
        return json.JSONEncoder.default(self,o)