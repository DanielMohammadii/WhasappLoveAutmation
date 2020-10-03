from twilio.rest import Client 
 
account_sid = 'ACa7a4b83e2896b6ac63584763048c6ccc' 
auth_token = '12072c34cbd497c6cf2082048fd18074' 
client = Client(account_sid, auth_token) 

def send_love(): 
    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body='This is Daniel\'s robot',      
                                to='whatsapp:+393892551792' 
                            ) 
    
    print(message.sid)