from fastapi import FastAPI
from src.backend.api.v1.routes.health import router as health_router

app = FastAPI(title="AFS WMS API", version="1.0")


@app.get("/")
def read_root():
    return {"message": "Welcome to AFS WMS API"}


app.include_router(health_router, prefix="/api/v1")
