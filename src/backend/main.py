from fastapi import FastAPI
from src.backend.api.v1.routes.health import router as health_router
from src.backend.api.v1.routes.inventory import router as inventory_router

app = FastAPI(title="AFS WMS API", version="1.0")

app.include_router(health_router, prefix="/api/v1")
app.include_router(inventory_router, prefix="/api/v1/inventory")
@app.get("/")
def read_root():
    return {"message": "Welcome to AFS WMS API"}


