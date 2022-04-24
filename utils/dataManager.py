import json

permanent = r"C:\Users\Killian Larcher\Documents\GitHub\RadiationCAM\datas\permanent_datas.json"
user = r"C:\Users\Killian Larcher\Documents\GitHub\RadiationCAM\datas\user_datas.json"


def getDatas(filename: str):
    global user, permanent
    file = user if filename == 'user' else permanent
    with open(file, "r") as f:
        datas = json.load(f)
        return datas


def updateData(filename: str, new_value: str):
    global user, permanent
    file = user if filename == 'user' else permanent
    with open(file, "w") as f:
        json.dump(new_value, f, indent=4)
