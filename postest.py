import requests

url = 'http://ec2-3-6-40-220.ap-south-1.compute.amazonaws.com:8090/'
myobj = {'percentage': '40','ID':'001','time':'6766767'}

x = requests.post(url, data = myobj)

print(x.text)