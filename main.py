from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class EmailModel(BaseModel):
    name: str
    contact: str
    message: str


@app.get("/")
def hello():
    return {"message": "FastAPI 101 START"}


@app.post("/email-server")
def send_email(emailModel: EmailModel):
    return {"code":"200","name": emailModel.name,"contact": emailModel.contact,"message": emailModel.message}