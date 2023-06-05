from fastapi import FastAPI, WebSocket
import asyncio
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
# import schedule
# from schedule import every, repeat
import random
import time

app = FastAPI()

origins = [
    "http://backend_sockets:8080",
    "http://localhost:8080",
    "http://front_react:3000",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def random_number():
        print("work done")
        return random.randint(1, 10)
#schedule.every(10).seconds.do(random_number)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    print("Accepting Connection")
    await websocket.accept()
    while True:
        await asyncio.sleep(10)
        payload = random_number()
        await websocket.send_json(payload)