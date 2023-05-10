from fastapi import FastAPI
from routers.flight import flight_router

app = FastAPI()

app.include_router(flight_router)