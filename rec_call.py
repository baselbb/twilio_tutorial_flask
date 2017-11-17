from flask import Flask
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)


@app.route("/voice", methods=['GET', 'POST'])
def voice():
    resp = VoiceResponse()

    resp.say("Hi Jan Smith, you received this message because you have an outstanding invoice with mansions management for USD 500 and 20 cents, please pay it as soon as possible")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

