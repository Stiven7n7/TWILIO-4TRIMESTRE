from email import message
from twilio.rest import Client
import keys

client = Client(keys.account_sid, keys.auth_token)

message = client.messages.create(
    body="AMA TOY TRIUNFANDO",
    from_=keys.twilio_number,
    to=keys.target_number
)

print(message.body)