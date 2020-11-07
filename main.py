from flask import Flask, request, Response
import logging
from twilio.rest import Client
import os 
import requests

app = Flask(__name__)
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
client = Client(account_sid, auth_token)

def send_whatsapp(message_sid, message_recipient):
    messageOri = client.messages(message_sid).fetch()
    message_body = messageOri.body
    message = client.messages.create(
                              body = message_body,
                              from_= 'whatsapp:+18178358402', #RSL APP Sender Number
                              to= 'whatsapp:' + message_recipient
                          )   

@app.route("/MessageStatus", methods=["POST"])
def incoming_sms():
    message_sid = request.values.get('MessageSid', None)
    message_status = request.values.get('MessageStatus', None)
    message_recipient = request.values.get('To', None)
    logging.info('SID: {}, Status: {}, To: {}'.format(message_sid, message_status, message_recipient))
    if message_status == 'delivered':
        send_whatsapp(message_sid, message_recipient)  
    return ('', 204)

if __name__ == "__main__":
    app.run(debug=True)