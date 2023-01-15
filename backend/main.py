import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from login.login import GithubOauth

SECRET = os.getenv("SECRET", default="my-secret")
app = FastAPI()
origin = os.getenv("UI_ORIGIN", default="http://localhost:3000")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin],
    allow_credentials=True,
    allow_methods=["GET", "POST", "DELETE"],
    allow_headers=["*"],
)
app.include_router(GithubOauth(SECRET).router)
