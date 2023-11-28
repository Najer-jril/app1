import json


def login(username, password):
    file = open("db.json", "r")
    data = json.load(file)
    prodi = username[0] + username[1]
    for i in data[prodi]:
        if i["NIM"] == username:
            if i["NIM"] == password:
                return i

    file.close()