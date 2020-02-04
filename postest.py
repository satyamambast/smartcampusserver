import requests

url = 'http://172.31.43.205:8888/'
myobj = {'percentage': '40','ID':'001','time':'6766767'}

x = requests.post(url, data = myobj)

print(x.text)