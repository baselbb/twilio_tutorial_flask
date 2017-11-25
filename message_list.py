# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import Client
from nums import *
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN
client = Client(account_sid, auth_token)

# A list of call objects with the properties described above

for message in client.messages.list():
    print(
        message.body,
        message.status,
        message.to,
        message.date_created,
        message.date_sent,
        message.error_code,
        message.error_message,
    )
