from fastapi import FastAPI
from pydantic import BaseModel
from mailjet_rest import Client
import os
app = FastAPI()

api_key ='<PLACE KEY HERE>'
api_secret= '<PLACE SECRET HERE>'

class EmailModel(BaseModel):
    name: str
    contact: str
    message: str

mailjet = Client(auth=(api_key, api_secret), version='v3.1')

@app.get("/")
def hello():
    return {"message": "FastAPI 101 START"}


@app.post("/email-server")
def send_email(emailModel: EmailModel):
    data = {
        'Messages': [
            {
            "From": {
                "Email": "<PLACE EMAIL HERE>",
                "Name": "<PLACE NAME HERE>"
            },
            "To": [
                {
                "Email": "<PLACE RECEIVE EMAIL HERE>",
                "Name": "<PLACE NAME HERE>"
                }
            ],
            "Subject": "<PLACE SUBJECT HERE>",
            "TextPart": "<PLACE MESSAGE BODY HERE>",
            "HTMLPart": "<h3>Dear passenger 1, welcome to <a href='https://www.mailjet.com/'>Mailjet</a>!</h3><br />May the delivery force be with you!",
            "CustomID": "AppGettingStartedTest"
            }
        ]
        }
    result = mailjet.send.create(data=data)
    return {"response": result.status_code}