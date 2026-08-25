from fastapi import FastAPI
from routes.transactions import router as transaction_router

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Merchant AI Autopilot API is running!"}


app.include_router(transaction_router)