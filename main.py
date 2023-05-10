from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
from mysql.connector import errorcode
from pydantic import BaseModel

app = FastAPI()
# Configuración CORS, para permitir el acceso desde diferentes orígenes
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class BoardingPass:
    def __init__(self, boardingPassId, purchaseId, passengerId, seatTypeId, seatId, flightId):
        self.boardingPassId = boardingPassId
        self.purchaseId = purchaseId
        self.passengerId = passengerId
        self.seatTypeId = seatTypeId
        self.seatId = seatId
        self.flightId = flightId


@app.get("/boarding_pass")
def get_boarding_passs():
    try:
        connection = mysql.connector.connect(user="bsale_test", password="bsale_test",
                                             host="mdb-test.c6vunyturrl6.us-west-1.rds.amazonaws.com",  database="airline", port="3306")
        print("Conexión exitosa a la base de datos")
    except mysql.connector.Error as e:
        print("Error al conectarse a la base de datos: {}".format(e))

    cursor = connection.cursor()
    connection.autoreconnect = True
    connection.pool_size = 5

    query = "SELECT * FROM boarding_pass"
    cursor.execute(query)

    results = cursor.fetchall()

    for row in results:
        print("boarding_pass_id: ", row[0])
        # print("purchase_id: ", row[1])
        # print("passenger_id: ", row[2])
        # print("seat_type_id: ", row[3])
        # print("flight_id: ", row[3])
        my_boarding_pass = BoardingPass(
            row[0], row[1], row[2], row[3], row[4], row[5])
        print(my_boarding_pass)

    cursor.close()
    connection.close()
    # print(results)
    return {"boarding_pass": results}


get_boarding_passs()

# app = FastAPI()
# app.title = "Reto técnico: Simulación check-in aerolínea"
# app.version = "0.0.1"

# boarding_passess = [
#     {
#             "boarding_pass_id": 1,
#             "purchase_id":69,
#             "passenger_id": 515,
#             "seat_type_id": 2,
#             "seat_id": 0,
#             "flight_id": 1
# 	},
#     {
#             "boarding_pass_id": 2,
#             "purchase_id":78,
#             "passenger_id": 423,
#             "seat_type_id": 3,
#             "seat_id": 0,
#             "flight_id": 2
# 	},
#     {
#             "boarding_pass_id": 7,
#             "purchase_id":141,
#             "passenger_id": 144,
#             "seat_type_id": 1,
#             "seat_id": 105,
#             "flight_id": 1
# 	},
#     {
#             "boarding_pass_id": 14,
#             "purchase_id":33,
#             "passenger_id": 529,
#             "seat_type_id": 1,
#             "seat_id": 4,
#             "flight_id": 4
# 	}
# ]

# class Flight(BaseModel):
#     flight_id:int
#     takeoff_date_time: int
#     takeoff_airport:str
#     landing_date_time: int
#     landing_airport: str
#     airplane_id: int

# flights = [
#     {
#             "flight_id": 1,
#             "takeoff_date_time": 1688207580,
#             "takeoff_airport": "Aeropuerto Internacional Arturo Merino Benitez, Chile",
#             "landing_date_time": 1688221980,
#             "landing_airport": "Aeropuerto Internacional Jorge Cháve, Perú",
#             "airplane_id": 1
# 	},
#     {
#             "flight_id": 2,
#             "takeoff_date_time": 1688491980,
#             "takeoff_airport": "Aeropuerto Internacional Jorge Cháve, Perú",
#             "landing_date_time": 1688495580,
#             "landing_airport": "Aeropuerto Francisco Carlé, Perú",
#             "airplane_id": 2
# 	}
# ]

# @app.get('/', tags=['home'])
# def message():
#     return HTMLResponse('<h1>Reto técnico: Simulación</h1>')

# @app.get("/boarding_pass")
# def get_boarding_passess():
#     return boarding_passess

# @app.get("/flights")
# def get_flights():
#     return flights

# @app.get("flights/{id}")
