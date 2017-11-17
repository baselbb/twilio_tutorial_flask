from flask import Flask, Response, request
from twilio import twiml
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from nums import *


app = Flask(__name__)

account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN

client = Client(account_sid, auth_token)

client.messages.create(
    to=PHONE_NUMBER,
    from_=TWILIO_NUMBER,
    body="Hi, this is management, you have USD 500 outstadning, reply Y if you already paid or M if you believe this is a mistake."
)


@app.route("/")
def check_app():
    # returns a simple string stating the app is working
    return Response("ngrok  works"), 200


@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()
    print(resp)

    # Determine the right reply for this message
    if body == 'Y':
        resp.message("Thank you, we will update our records!")
    elif body == 'M':
        resp.message("Thanks you, we will check our system for the error")
    else:
        resp.message("Good Bye!")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
