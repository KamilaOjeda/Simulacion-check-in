import mysql.connector
from mysql.connector import errorcode


class Database:
    def __init__(self):
        self.connection = None
    
    def connection(self):
        try:
            self.connection = mysql.connector.connect(user="bsale_test",
    password= "bsale_test",
    host= "mdb-test.c6vunyturrl6.us-west-1.rds.amazonaws.com",
    database= "airline",
    port= "3306")
            print("La conexión fue exitosa")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Acceso denegado")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("La base de datos no existe")
            else:
                print("Ha ocurrido un error")

    def disconnection(self):
        self.connection.close()
    

                