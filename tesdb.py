import json


file = open("db.json", "r")
data = json.load(file)

def get_data_by_nim(nim):
    prodi = nim[0] + nim[1]
    for i in data[prodi]:
        if i["NIM"] == nim:
            return i
        
def update_skor(nim):
    prodi = nim[0] + nim[1]
    for i in data[prodi]:
        if i["NIM"] == nim:
            return i
    

file.close()