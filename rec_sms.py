import os
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

from nums import *

app = Flask(__name__)


account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN

client = Client(account_sid, auth_token)

client.messages.create(
    to=PHONE_NUMBER,
    from_=TWILIO_NUMBER,
    body="Hi, this is test, reply Y if you already paid"
)


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    resp = MessagingResponse()

    resp.message("Ok, thanks will update our files")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
