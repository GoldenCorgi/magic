from typing import Optional

from fastapi import FastAPI
import uvicorn
import os
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get("")
def read_root():
    return RedirectResponse("/docs")
@app.get("/")
def read_root2():
    return RedirectResponse("/docs")

RAM_frontend = []
RAM_hardware = []

@app.post("/frontend/push_data")
def frontend_push_data(data: Optional[dict] = None):
    RAM_frontend.append(data)
    return True

@app.get("/frontend/get_data")
def frontend_get_data():
    return RAM_hardware

@app.get("/hardware/get_data")
def hardware_get_data():
    return RAM_frontend

@app.post("/hardware/push_data")
def hardware_push_data(data: Optional[dict] = None):
    RAM_hardware.append(data)
    return True
port = int(os.getenv('PORT', 8000))

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=port, log_level="info")
