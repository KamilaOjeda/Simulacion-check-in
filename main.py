from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
from mysql.connector import errorcode

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

@app.get("/flight")
async def get_flights():
    try:
        connection = mysql.connector.connect(user = "test", password = "test", host = "hostdeamazon.com",  database = "pruebadatabase", port = "3306")
        print("Conexión exitosa a la base de datos")
    except mysql.connector.Error as e:
        print("Error al conectarse a la base de datos: {}".format(e))

    cursor = connection.cursor()
    connection.autoreconnect = True
    connection.pool_size = 5

    query = "SELECT * FROM flight"
    cursor.execute(query)

    results = cursor.fetchall()

    cursor.close()
    connection.close()
    
    return {"flight": results}