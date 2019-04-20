import requests
import json 
from requests.auth import HTTPBasicAuth

url = "http://localhost:8080/restapp/predict/"

payload = {"petal_length":"0.1","petal_width":"2.134","sepal_length":"0.124","sepal_width":"0.123"}
headers = {
            'media_type': "application/json",
                'Content-Type': "application/json",
                    'cache-control': "no-cache",
                        'Postman-Token': "4b07d5f3-0fcf-465d-8581-0e61e3cfe4e4"
                            }

print(json.dumps(payload))
response = requests.request("POST", url, data=json.dumps(payload), headers=headers, auth=('deltaHell96','gemini@76y2'))

print(response.text)
