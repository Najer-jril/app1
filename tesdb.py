import json



def get_data_by_nim(nim):
    file = open("db.json", "r")
    data = json.load(file)
    prodi = nim[0] + nim[1]
    for i in data[prodi]:
        if i["NIM"] == nim:
            return i

    file.close()