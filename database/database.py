# import mysql.connector
# from mysql.connector import errorcode
# from fastapi import HTTPException
# from fastapi.responses import JSONResponse
# from fastapi import status
# from config.config import DB_CONFIG


# class Database:
#     def __init__(self):
#         try:
#             self.connection = mysql.connector.connect(**DB_CONFIG)
#             print("Conexión exitosa a la base de datos")
#         except mysql.connector.Error as e:
#             print(f"Error al conectarse a la base de datos: {e}")
#             raise HTTPException(
#                 status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#                 detail="Error al conectarse a la base de datos"
#             )

#     def execute_query(self, query):
#         try:
#             cursor = self.connection.cursor()
#             cursor.execute(query)
#             results = cursor.fetchall()
#             cursor.close()
#             return results
#         except mysql.connector.Error as e:
#             print(f"Error al ejecutar la consulta: {e}")
#             raise HTTPException(
#                 status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#                 detail="Error al ejecutar la consulta"
#             )
