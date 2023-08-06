from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import process

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(process.router)
