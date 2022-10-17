import uvicorn
from celery import Celery
from fastapi import FastAPI

app = FastAPI()

worker = Celery(broker='amqp://guest:guest@localhost:5672//')
counter = 0

@app.get("/")
def home():
    worker.send_task("task")

@worker.task(name="task")
def task():
    global counter
    counter += 1
    print("Hello World", counter)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
