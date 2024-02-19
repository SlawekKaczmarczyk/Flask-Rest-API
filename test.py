import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "video/1", {"rating": 9, "name": "Slawek","views": 214237})
print(response.json())
input()
response = requests.get(BASE + "video/1", {"rating": 9})
print(response.json())