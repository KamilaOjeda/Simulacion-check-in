from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
from mysql.connector import errorcode
from pydantic import BaseModel

# Configuración CORS, para permitir el acceso desde diferentes orígenes 
# origins = [
#     "http://localhost",
#     "http://localhost:8000",
#     "http://localhost:8080",
#     "http://localhost:3000",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# @app.get("/boarding_pass")
# async def get_boarding_passs():
#     try:
#         connection = mysql.connector.connect(user = "bsale_test", password = "bsale_test", host = "mdb-test.c6vunyturrl6.us-west-1.rds.amazonaws.com",  database = "airline", port = "3306")
#         print("Conexión exitosa a la base de datos")
#     except mysql.connector.Error as e:
#         print("Error al conectarse a la base de datos: {}".format(e))

#     cursor = connection.cursor()
#     connection.autoreconnect = True
#     connection.pool_size = 5

#     query = "SELECT * FROM boarding_pass"
#     cursor.execute(query)

#     results = cursor.fetchall()

#     cursor.close()
#     connection.close()
    
#     return {"boarding_pass": results}

app = FastAPI()
app.title = "Reto técnico: Simulación check-in aerolínea"
app.version = "0.0.1"
class Boarding(BaseModel):
    boarding_pass_id: int
    purchase_id:int
    passenger_id: int
    seat_type_id: int
    seat_id: int
    flight_id:int

boarding_passess = [
    {
            "boarding_pass_id": 1,
            "purchase_id":69,
            "passenger_id": 515,
            "seat_type_id": 2,
            "seat_id": 0,
            "flight_id":1
	},
    {
            "boarding_pass_id": 2,
            "purchase_id":78,
            "passenger_id": 423,
            "seat_type_id": 3,
            "seat_id": 0,
            "flight_id":2
	}
]

@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Reto técnico: Simulación</h1>')

@app.get("/boarding_pass")
def get_boarding_passess():
    return boarding_passess