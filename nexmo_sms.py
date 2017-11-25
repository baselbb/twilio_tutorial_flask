import nexmo
from nums import *

client = nexmo.Client(key=NEXMO_KEY, secret=NEXMO_AUTH)

client.send_message({
    'from': 'Nexmo',
    'to': PHONE_NUMBER,
    'text': 'Hello world'
})


