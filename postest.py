import requests

url = 'http://122.174.136.121:54300/'
myobj = {'percentage': '40','ID':'001','time':'6766767'}

x = requests.post(url, data = myobj)

print(x.text)