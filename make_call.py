import os
from twilio.rest import Client

from nums import *

account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN

client = Client(account_sid, auth_token)

call = client.calls.create(
    to=PHONE_NUMBER,
    from_=TWILIO_NUMBER,
    url="http://demo.twilio.com/docs/voice.xml"
)

print(call.sid)

