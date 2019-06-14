import urllib.request
import urllib.parse
 
def sendSMS(apikey, numbers, sender, message):
    data =  urllib.parse.urlencode({'apikey': 'e6XWqkLCgYM-5Pg78C9cG7L8aGtXzHyoT89ulj7bDf', 'numbers': '7702508581',
        'message' : 'AGNEYA Crash alert  : Location:  http://www.google.com/maps/place/30.767690,76.575402 \n Driver:  Thomas Thoppill \n Vehicle ID : ESVC 19 A-43'})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return(fr)
 
resp =  sendSMS('apikey', '918123456789',
    'Jims Autos', 'This is your message')
print (resp)
