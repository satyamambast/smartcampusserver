import requests

url = 'http://localhost:8889/'
myobj = {'percentage': '40','ID':'001','time':'6766767'}

x = requests.post(url, data = myobj)

print(x.text)