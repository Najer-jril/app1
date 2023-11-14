import json

with open('db.json', 'r') as file:
    user_data = json.load(file)

file = open("db.json", "r")
data = json.load(file)

def login(username):
    prodi = username[0] + username[1]
    for i in data[prodi]:
        if i["NIM"] == username:
            return i