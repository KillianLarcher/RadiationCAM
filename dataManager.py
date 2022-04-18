import json

permanent = r"C:\Users\Killian Larcher\Documents\GitHub\RadiationCAM\datas\permanent_datas.json"
user = r"C:\Users\Killian Larcher\Documents\GitHub\RadiationCAM\datas\user_datas.json"


def updateData(filename, key, value):
    global user, permanent
    file = user if filename == 'user' else permanent
    with open(file, "r") as f:
        datas = json.load(f)
    datas[key] = value
    with open(file, "w") as f:
        json.dump(datas, f, indent=4)


def getData(filename, key):
    global user, permanent
    file = user if filename == 'user' else permanent
    with open(file, "r") as f:
        datas = json.load(f)
        return datas[key]


def getDatas(filename):
    global user, permanent
    file = user if filename == 'user' else permanent

    with open(file, "r") as f:
        datas = json.load(f)
        return datas
