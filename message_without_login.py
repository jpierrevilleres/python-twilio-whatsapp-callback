from twilio.rest import Client
from helpers import lookup
import os 
import requests

account_sid = "###"  # Your Account SID from www.twilio.com/console
api_key = "###"  # You can generate this from www.twilio.com/console/runtime/api-keys/create
api_secret = "###" # You can generate this from www.twilio.com/console/runtime/api-keys/create

# DANGER! This is insecure. See http://twil.io/secure
client = Client(api_key, api_secret, account_sid)

# Proof request to check credentials are working.
# Retrieving your account information
accounts = client.api.accounts.list()
for record in accounts:
    print(record.sid)

message = client.messages.create(
                              body='Thank you for using RSL APP. As part of the cashback campaign, We have refunded 50 AED as wallet amount to your passenger app account.',
                              #from_='whatsapp:+14155238886', Sandbox Whatsapp
                              from_='whatsapp:+18178358402', #RSL App Whatsapp
                              #to='whatsapp:+919789229442', Sathish
                              to='whatsapp:+919789229442',
                          )
print(message.sid)                    

#response = requests.get(f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages/{message.sid}.json")
#print(response)
