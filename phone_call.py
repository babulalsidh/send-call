from twilio.rest import Client

# Your Twilio credentials
account_sid = 'ACe57367f49ac375f103b4d2840e045452'
auth_token = '33d99a27f79a668f75027951d26554544e'
client = Client(account_sid, auth_token)

call = client.calls.create(
    twiml='<Response><Say>Hi babu, this is your Copilot saying hello!</Say></Response>',
    to='+91123456789',          # Replace with the recipient's phone number
    from_='+14105083003'         # Your Twilio number
)

print(f"Call initiated! SID: {call.sid}")
