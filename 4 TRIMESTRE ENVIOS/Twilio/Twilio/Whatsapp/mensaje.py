from http import client
from twilio.rest import Client



auth_token = "6d9322c6a48b6a88b29aceb528313c7a"
sid_id = "AC3c2f96e1ecb692167b018bce5cc37859"
client = Client(sid_id,auth_token)

from_whatsapp_number='whatsapp:+14155238886'

to_whatsapp_number='whatsapp:+573046542429'

client.messages.create(
    body='holiiiiiiiiii',
    from_=from_whatsapp_number,
    to=to_whatsapp_number
)