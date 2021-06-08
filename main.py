from typing import Optional

from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return True

RAM_frontend = []
RAM_hardware = []

@app.post("/frontend/push_data")
def frontend_push_data(data: Optional[dict] = None):
    RAM_frontend.append(data)
    return True

@app.get("/frontend/get_data}")
def frontend_get_data():
    return RAM_hardware

@app.get("/hardware/get_data}")
def hardware_get_data():
    return RAM_frontend

@app.post("/hardware/push_data}")
def hardware_push_data(data: Optional[dict] = None):
    RAM_hardware.append(data)
    return True

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80, log_level="info")
