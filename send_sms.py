import os
from twilio.rest import Client
from nums import *

account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN

client = Client(account_sid, auth_token)

client.messages.create(
    to=PHONE_NUMBER,
    from_=TWILIO_NUMBER,
    body="Hi, this is test, reply Y if you already paid"
)
