import json

permanent = './datas/permanent_datas.json'
user = './datas/user_datas.json'


def getDatas(filename: str):
    global user, permanent
    file = user if filename == 'user' else permanent
    with open(file, "r", encoding='utf-8') as f:
        datas = json.load(f)
        return datas


def updateData(filename: str, new_value: str):
    global user, permanent
    file = user if filename == 'user' else permanent
    with open(file, "w") as f:
        json.dump(new_value, f, indent=4)
