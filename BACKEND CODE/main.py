from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    user_input: str

@app.get("/")
def home():
    return {"message": "Backend is running"}

@app.post("/process")
def process_data(data: InputData):
    return {
        "output": f"You entered: {data.user_input}"
    }
