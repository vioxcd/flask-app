import json
import requests

url = 'http://httpbin.org/post'
payload = {'colors': [
        {"color": "green", "hex": "#0f0"},
        {"color": "blue", "hex": "#00f"},
        {"color": "cyan", "hex": "#0ff"},
        {"color": "magenta", "hex": "#f0f"},
        {"color": "yellow", "hex": "#ff0"},
        {"color": "black", "hex": "#000"}
        ]}
headers = {'content-type': 'application/json'}

# post data to a web server
response = requests.post(url, data=json.dumps(payload), headers=headers)

print(response.status_code)
