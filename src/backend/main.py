from fastapi import FastAPI

app = FastAPI(title="AFS WMS API", version="1.0")

@app.get("/")
def read_root():
    return {"message": "Welcome to AFS WMS API"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
