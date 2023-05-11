from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
from schemas.boarding_pass import BoardingPass
from schemas.passenger_with_pass import PassengerWithBoardingPass, PassengerWithBoardingPassEncoder
from typing import List
import json

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

def get_connection():
    try:
        connection = mysql.connector.connect(
            user="bsale_test", 
            password="bsale_test", 
            host="mdb-test.c6vunyturrl6.us-west-1.rds.amazonaws.com",  
            database="airline", 
            port="3306")
        print("Conexión exitosa a la base de datos")
            
    except mysql.connector.Error as e:
        print("Error al conectarse a la base de datos: {}".format(e)) 
        
    connection.autoreconnect = True
    connection.pool_size = 5
    return connection
 
my_connection = get_connection()
cursor = my_connection.cursor()

def transform_to_boarding_pass(row):
    return BoardingPass(row[0], row[1], row[2], row[3], row[4], row[5])

def get_passenger_from_boarding_pass(boarding_pass: BoardingPass) -> PassengerWithBoardingPass:
    query = f"SELECT * FROM passenger WHERE passenger_id = {boarding_pass.passengerId}".format(boarding_pass.passengerId)
    cursor.execute(query)
    row = cursor.fetchone()
    return PassengerWithBoardingPass(row[0], row[1], row[2], row[3], row[4], boarding_pass.boardingPassId, boarding_pass.purchaseId, boarding_pass.seatTypeId, boarding_pass.seatId)

def get_boarding_pass_list_by_flight_by_id(id: int):
    query = f"SELECT * FROM boarding_pass WHERE flight_id = {id}".format(id)
    cursor.execute(query)

    result = cursor.fetchall()
    my_boarding_pass_list = map(transform_to_boarding_pass, result)
    return list(my_boarding_pass_list)

def get_passenger_list_from_bording_pass_list(boarding_pass_list: List[BoardingPass]):
    passenger_list = map(get_passenger_from_boarding_pass, boarding_pass_list)
    return list(passenger_list)

@app.get("/passengers_with_boarding_pass")
def get_passengers_with_boarding_pass():
    my_boarding_pass_list = get_boarding_pass_list_by_flight_by_id(1)

    my_passengers = get_passenger_list_from_bording_pass_list(my_boarding_pass_list)
    my_connection.close()
    cursor.close()
    rpta = json.dumps(my_passengers, cls=PassengerWithBoardingPassEncoder)
    return {"my_boarding_pass_list": rpta}
