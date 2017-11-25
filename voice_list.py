# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import Client
from nums import *
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN
client = Client(account_sid, auth_token)

# A list of call objects with the properties described above
for call in client.calls.list():
    print(call.sid,
          call.date_created,
          # call.date_updated,
          # call.from_,
          call.to,
          call.status,
          # call.start_time,
          # call.end_time,
          call.duration,
          # call.direction,
          call.answered_by,
          # call.forwarded_from,
          # call.caller_name,
    )
