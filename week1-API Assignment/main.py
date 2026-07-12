from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Hello FlyRank! This is Mujtaba(flyrank internee) and this is my first API assignment."
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }