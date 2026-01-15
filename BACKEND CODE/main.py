from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    user_input: str

@app.post("/process")
def process_data(data: InputData):
    return {"output": f"You entered: {data.user_input}"}

@app.get("/", response_class=HTMLResponse)
def serve_frontend():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

