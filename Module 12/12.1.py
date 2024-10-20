import requests
import json

request = "https://api.chucknorris.io/jokes/random"
response = requests.get(request).json()
print(json.dumps(response,indent = 4))
print(response['value'])
