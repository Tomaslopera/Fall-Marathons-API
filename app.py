from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.marathons import marathon

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://localhost:8000"
]

app.include_router(marathon)