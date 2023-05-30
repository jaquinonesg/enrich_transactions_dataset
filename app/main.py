from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import enrich_data


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(enrich_data.router)


@app.get(path="/")
def root():
    return {"message": "Its alive"}
