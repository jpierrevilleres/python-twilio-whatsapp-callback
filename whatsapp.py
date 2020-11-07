from twilio.rest import Client
from helpers import lookup
import os 
import requests

account_sid = os.environ.get("ACCOUNT_SID")
api_key = os.environ.get("API_KEY")
api_secret = os.environ.get("API_SECRET")
auth_token = os.environ.get("AUTH_TOKEN")

client = Client(account_sid, auth_token)

message = client.messages('SM3d604cb879e1484eaee09edd01fd7965').fetch()

#numbers_to_message = ['whatsapp:+971528067285', 'whatsapp:+971564833933']
#for number in numbers_to_message:
message = client.messages.create(
                              body = message.body,
                              from_= 'whatsapp:+18178358402', #RSL APP Sender Number
                              to='whatsapp:+919789229442',
                          )
print(message.sid)                           