import json

permanent = r"C:\Users\Killian Larcher\Documents\GitHub\RadiationCAM\datas\permanent_datas.json"
user = r"C:\Users\Killian Larcher\Documents\GitHub\RadiationCAM\datas\user_datas.json"


def updateData(filename: str, category: str, new_value: dict):
    global user, permanent
    file = user if filename == 'user' else permanent
    with open(file, "r") as f:
        datas = json.load(f)
    datas[category] = new_value
    with open(file, "w") as f:
        json.dump(datas, f, indent=4)



def getDatas(filename: str):
    global user, permanent
    file = user if filename == 'user' else permanent
    with open(file, "r") as f:
        datas = json.load(f)
        return datas
