import requests

BASE = "http://127.0.0.1:5000/"


data = [{"rating": 9, "name": "Godfahter", "views": 21427},
        {"rating": 10, "name": "Godfahter 2", "views": 24237},
        {"rating": 8, "name": "Godfahter 3", "views": 1437}]


for i in range(len(data)):
    response = requests.put(BASE + "video/" +str(i), data[i])
    print(response.json())

input()
response = requests.delete(BASE + "video/0")
print(response.json)
#input()
response = requests.get(BASE + "video/6")
print(response.json())