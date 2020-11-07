from twilio.rest import Client
import os 

account_sid = os.environ.get("ACCOUNT_SID")
api_key = os.environ.get("API_KEY")
api_secret = os.environ.get("API_SECRET")

client = Client(api_key, api_secret, account_sid)

message = client.messages \
    .create(
         body='Congratz! Your RSL APP Wallet is credited with AED 50 as a part of our cashback campaign. Hurry up. Book a ride now and pay with your wallet. http://onelink.to/rslapp',
         from_='+18178358402',
         to='+971522379218'
     )

print(message.sid)