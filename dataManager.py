import json

fichier = r"C:\Users\Killian Larcher\Documents\GitHub\RadiationCAM\datas.json"


def updateData(key, value):
    with open(fichier, "r") as f:
        datas = json.load(f)
    datas[key] = value
    with open(fichier, "w") as f:
        json.dump(datas, f, indent=4)
