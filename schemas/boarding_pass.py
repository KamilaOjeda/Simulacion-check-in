from pydantic import BaseModel, Field

class BoardingPass:
    def __init__(self, boardingPassId, purchaseId, passengerId, seatTypeId, seatId, flightId):
        self.boardingPassId = boardingPassId
        self.purchaseId = purchaseId
        self.passengerId = passengerId
        self.seatTypeId = seatTypeId
        self.seatId = seatId
        self.flightId = flightId