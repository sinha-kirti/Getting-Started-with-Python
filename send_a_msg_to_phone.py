from twilio.rest import TwilioRestClient

account_sid = "AC4*****************************" # Your Account SID from www.twilio.com/console
auth_token  = "99******************************"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    body="Hello! You  have got a message from Twilio",
    to="+9198********",    # Replace with your phone number
    from_="+165********") # Replace with your Twilio number
print(message.sid)
