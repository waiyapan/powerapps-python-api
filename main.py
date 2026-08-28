from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI(
    title="Power Apps Python API",
    version="1.0"
)


class PowerAppRequest(BaseModel):
    name: str
    message: str


@app.get("/")
def home():
    return {
        "status": "online",
        "message": "Python API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.post("/process")
def process_data(data: PowerAppRequest):

    print(f"Received from: {data.name}")
    print(f"Message: {data.message}")

    result_message = (
        f"Hello {data.name}! "
        f"Python API received: {data.message}"
    )

    return {
        "status": "success",
        "result": result_message,
        "processed_at": datetime.now().isoformat()
    }
