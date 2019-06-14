from twilio.rest import Client

account_sid = "AC8bdc93885c465f8192af56133450ca45"
auth_token = "1e813ba28df63b4d31073ed8a23181d1"

client = Client(account_sid , auth_token)

message  = client.api.account.messages.create(
                to ="+917702508581",
                from_ ="+12132386668",
                body = "Crash alert  : Location:  http://www.google.com/maps/place/30.767690,76.575402  Driver:  details"
                )
    
