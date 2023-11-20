import json


file = open("rule1.json", "r")
data = json.load(file)

def load_rules():
    return data["rule"]

    
file.close()
