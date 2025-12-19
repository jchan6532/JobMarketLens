#Developers: Justin Chan, Philip Wojdyna
#Date: December 18, 2025
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Backend running"}
