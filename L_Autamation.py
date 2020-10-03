from twilio.rest import Client 
 
account_sid = 'your-sid' 
auth_token = 'Auth-token' 
client = Client(account_sid, auth_token) 

def send_love(): 
    message = client.messages.create( 
                                from_='whatsapp:+14111111',  
                                body='This is Daniel\'s robot',      
                                to='whatsapp:+354547999668' 
                            ) 
    
    print(message.sid)
