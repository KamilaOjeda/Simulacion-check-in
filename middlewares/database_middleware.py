# from typing import Optional
# from fastapi import Request, HTTPException
# from database.database import Database


# class DatabaseMiddleware:
#     def __init__(self, app, db: Database):
#         self.app = app
#         self.db = db

#     async def __call__(self, request: Request, next):
#         try:
#             # Si la conexión está inactiva por más de 5 segundos, se reconecta automáticamente
#             if not self.db.is_connected():
#                 self.db.connect()
#             response = await next(request)
#         except Exception as e:
#             # En caso de error, se cierra la conexión a la base de datos
#             self.db.disconnect()
#             raise HTTPException(status_code=500, detail="Internal server error")
#         return response
