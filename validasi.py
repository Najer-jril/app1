import json

with open('useroradmin.json', 'r') as file:
    user_data = json.load(file)

file = open("db.json", "r")
data = json.load(file)

def login(username, password):
    prodi = username[0] + username[1]
    for i in data[prodi]:
        if i["NIM"] == username:
            return i
        
    # for user in user_data.get("users"):
    #     valid = user["username"] == username and user["password"] == password
    #     if valid and user["role"] ==  "admin" :
    #         return "admin"
    #     elif valid:
    #         return "user"
    # else:
    #     return False
    

if __name__ == "__main__":
    login()
