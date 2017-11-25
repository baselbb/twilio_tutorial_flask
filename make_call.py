import os
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse

from nums import *

account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN

calls_list = []


client = Client(account_sid, auth_token)

print('Making a call....')
call = client.calls.create(
    to=PHONE_NUMBER,
    from_=TWILIO_NUMBER,
    machine_detection="Enable",
    url='https://handler.twilio.com/twiml/EH50a0f05c66c9cfa7d00c090d8aee3423'
)

message_detail = (call.sid,
                  call.date_created,
                  call.date_updated,
                  call.from_,
                  call.to,
                  call.status,
                  call.start_time,
                  call.end_time,
                  call.duration,
                  call.direction,
                  call.answered_by,
                  call.forwarded_from,
                  )

print(message_detail)

call_sid = message_detail[0]
print(call_sid)
call = client.calls(call_sid).fetch()
print(call)



