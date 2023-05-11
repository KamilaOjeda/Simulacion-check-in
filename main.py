from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
from schemas.boarding_pass import BoardingPass
from schemas.passenger_with_pass import PassengerWithBoardingPass, PassengerWithBoardingPassEncoder
from typing import List
import json
import asyncio

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
async def get_connection():
    try:
        connection = await mysql.connector.connect(
            user="bsale_test", 
            password="bsale_test", 
            host="mdb-test.c6vunyturrl6.us-west-1.rds.amazonaws.com",  
            database="airline", 
            port="3306")
        print("Conexión exitosa a la base de datos")
            
    except mysql.connector.Error as e:
        print("Error al conectarse a la base de datos: {}".format(e)) 
        
    connection.autoreconnect = True
    connection.pool_size = 30
    return connection

    
async def transform_to_boarding_pass(row):
    return await BoardingPass(row[0], row[1], row[2], row[3], row[4], row[5])

async def get_passenger_from_boarding_pass(boarding_pass: BoardingPass, cursor) -> PassengerWithBoardingPass:
    query = f"SELECT * FROM passenger WHERE passenger_id = {boarding_pass.passengerId}".format(boarding_pass.passengerId)
    cursor.execute(query)
    row = await cursor.fetchone()
    return PassengerWithBoardingPass(row[0], row[1], row[2], row[3], row[4], boarding_pass.boardingPassId, boarding_pass.purchaseId, boarding_pass.seatTypeId, boarding_pass.seatId)

async def get_boarding_pass_list_by_flight_by_id(id: int, cursor):
    query = f"SELECT * FROM boarding_pass WHERE flight_id = {id} LIMIT 1".format(id)
    cursor.execute(query)

    result = await cursor.fetchall()
    my_boarding_pass_list = map(transform_to_boarding_pass, result)
    return list(my_boarding_pass_list)

async def get_passenger_list_from_bording_pass_list(boarding_pass_list: List[BoardingPass], cursor):
    passenger_list = map(get_passenger_from_boarding_pass(cursor=cursor), boarding_pass_list)
    return list(passenger_list)

async def main():
    my_connection = get_connection()
    cursor = await my_connection.cursor()
    my_boarding_pass_list = get_boarding_pass_list_by_flight_by_id(1, cursor)
    my_passengers = get_passenger_list_from_bording_pass_list(my_boarding_pass_list, cursor)
    my_connection.close()
    rpta = json.dumps(my_passengers, cls=PassengerWithBoardingPassEncoder)

    print(rpta)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()

       
# @app.get("/boarding_pass")
# def get_boarding_passs(): 
#     connection = get_connection()
#     query = "SELECT * FROM boarding_pass"
#     cursor = connection.cursor()
#     cursor.execute(query)

#     results = cursor.fetchall()

#     for row in results:
#         my_boarding_pass = BoardingPass(
#             row[0], row[1], row[2], row[3], row[4], row[5])
#         print(my_boarding_pass)

#     connection.close()
#     return {"boarding_pass": results}

# get_boarding_passs()

# @app.get("/flights")
# def get_flights(): 
#     connection = get_connection()
#     query = "SELECT * FROM flights"
#     cursor = connection.cursor()
#     cursor.execute(query)

#     results = cursor.fetchall()

#     for row in results:
#         flights = Flight(
#             row[0], row[1], row[2], row[3], row[4], row[5])
#         print(flights)

#     connection.close()
#     # print(results)
#     return {"flights": results}

# # get_flights()

# @app.get("/passengers")
# def get_passengers(): 
#     connection = get_connection()
#     query = "SELECT * FROM passengers"
#     cursor = connection.cursor()
#     cursor.execute(query)

#     results = cursor.fetchall()

#     for row in results:
#         passengers = Passenger(
#             row[0], row[1], row[2], row[3], row[4])
#         print(passengers)

#     connection.close()
#     # print(results)
#     return {"passengers": results}

# # get_passengers()

# @app.get("/purchases")
# def get_purchases(): 
#     connection = get_connection()
#     query = "SELECT * FROM purchases"
#     cursor = connection.cursor()
#     cursor.execute(query)

#     results = cursor.fetchall()

#     for row in results:
#         purchases = Purchase(
#             row[0], row[1])
#         print(purchases)

#     connection.close()
#     # print(results)
#     return {"purchases": results}

# # get_purchases()

# @app.get("/seats")
# def get_seats(): 
#     connection = get_connection()
#     query = "SELECT * FROM seats"
#     cursor = connection.cursor()
#     cursor.execute(query)

#     results = cursor.fetchall()

#     for row in results:
#         seats = Seat(
#             row[0], row[1], row[2], row[3], row[4])
#         print(seats)

#     connection.close()
#     # print(results)
#     return {"seats": results}

# # get_seats()

# @app.get("/seats_type")
# def get_seats_type(): 
#     connection = get_connection()
#     query = "SELECT * FROM seats_type"
#     cursor = connection.cursor()
#     cursor.execute(query)

#     results = cursor.fetchall()

#     for row in results:
#         seats_type = SeatType(
#             row[0], row[1], row[2])
#         print(seats_type)

#     connection.close()
#     # print(results)
#     return {"seats_type": results}

# # get_seats_type()

# @app.get("/airplanes")
# def get_airplanes(): 
#     connection = get_connection()
#     query = "SELECT * FROM airplanes"
#     cursor = connection.cursor()
#     cursor.execute(query)

#     results = cursor.fetchall()

#     for row in results:
#         airplanes = Airplane(
#             row[0], row[1])
#         print(airplanes)

#     connection.close()
#     # print(results)
#     return {"airplanes": results}

# # get_airplanes()


# def get_flight_by_id(id: int): 
#     connection = get_connection()
#     query = f"SELECT * FROM flight WHERE flight_id = {id}".format(id)
#     cursor = connection.cursor()
#     cursor.execute(query)

#     result = cursor.fetchall()

#     connection.close()
#     return result

# print(get_flight_by_id(1))


# # app = FastAPI()
# # app.title = "Reto técnico: Simulación check-in aerolínea"
# # app.version = "0.0.1"

# # boarding_passess = [
# #     {
# #             "boarding_pass_id": 1,
# #             "purchase_id":69,
# #             "passenger_id": 515,
# #             "seat_type_id": 2,
# #             "seat_id": 0,
# #             "flight_id": 1
# # 	},
# #     {
# #             "boarding_pass_id": 2,
# #             "purchase_id":78,
# #             "passenger_id": 423,
# #             "seat_type_id": 3,
# #             "seat_id": 0,
# #             "flight_id": 2
# # 	},
# #     {
# #             "boarding_pass_id": 7,
# #             "purchase_id":141,
# #             "passenger_id": 144,
# #             "seat_type_id": 1,
# #             "seat_id": 105,
# #             "flight_id": 1
# # 	},
# #     {
# #             "boarding_pass_id": 14,
# #             "purchase_id":33,
# #             "passenger_id": 529,
# #             "seat_type_id": 1,
# #             "seat_id": 4,
# #             "flight_id": 4
# # 	}
# # ]

# # class Flight(BaseModel):
# #     flight_id:int
# #     takeoff_date_time: int
# #     takeoff_airport:str
# #     landing_date_time: int
# #     landing_airport: str
# #     airplane_id: int

# # flights = [
# #     {
# #             "flight_id": 1,
# #             "takeoff_date_time": 1688207580,
# #             "takeoff_airport": "Aeropuerto Internacional Arturo Merino Benitez, Chile",
# #             "landing_date_time": 1688221980,
# #             "landing_airport": "Aeropuerto Internacional Jorge Cháve, Perú",
# #             "airplane_id": 1
# # 	},
# #     {
# #             "flight_id": 2,
# #             "takeoff_date_time": 1688491980,
# #             "takeoff_airport": "Aeropuerto Internacional Jorge Cháve, Perú",
# #             "landing_date_time": 1688495580,
# #             "landing_airport": "Aeropuerto Francisco Carlé, Perú",
# #             "airplane_id": 2
# # 	}
# # ]

# # @app.get('/', tags=['home'])
# # def message():
# #     return HTMLResponse('<h1>Reto técnico: Simulación</h1>')

# # @app.get("/boarding_pass")
# # def get_boarding_passess():
# #     return boarding_passess

# # @app.get("/flights")
# # def get_flights():
# #     return flights

# # @app.get("flights/{id}")
