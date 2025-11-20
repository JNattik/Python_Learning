from twilio.rest import Client

account_sid = 'AC6df10d0aab88daf6a09db83f673b5aca'
auth_token = 'e5875f7a3da177dfe1a705cb84f0a8b0'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  content_sid='HXb5b62575e6e4ff6129ad7c8efe1f983e',
  content_variables='{"1":"12/1","2":"3pm"}',
  to='whatsapp:+4916093918341'
)

print(message.sid)