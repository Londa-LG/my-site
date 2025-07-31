from models import Base
from connect import engine
from fastapi import FastAPI
from routers import profile, projects
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:8000",
    "http://localhost:8080",
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"]
)

Base.metadata.create_all(bind=engine)

app.include_router(profile.router)
app.include_router(projects.router)

