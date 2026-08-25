from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Merchant AI Autopilot API is running!"}
