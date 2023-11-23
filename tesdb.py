import json


file = open("db.json", "r")
data = json.load(file)

def get_data_by_nim(nim):
    prodi = nim[0] + nim[1]
    for i in data[prodi]:
        if i["NIM"] == nim:
            return i
# def update():
#     open("db.json", "r")
    
    
    # def update_skor(pilih):
    #     file2 = open("rule1.json", "r")
    #     skor = json.load(file2)\
    #     nim = self.Ledit_NIM.text()
    #     data = tesdb.get_data_by_nim(nim)
    #     rules = skor["rule"]
    #     i["skor"] += rules[pilih]["poin"]



        
# def update_skor(nim):
#     prodi = nim[0] + nim[1]
#     for i in data[prodi]:
#         if i["NIM"] == nim:
#             return i
    

file.close()