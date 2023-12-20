import json

class Leuk:
    def __init__(self, id, name, cost):
        self.data = {
            "lekarsva_id": f'{id}',
            "lekarsva_name": f'{name}',
            "lekarsva_cost": f'{cost}'
        }
class Postoyal:
    def __init__(self, id, fio, data_rog, id_lek):
        self.data = {
            "postoyal_pok_id": f'{id}',
            "postoyal_pok_fio": f'{fio}',
            "postoyal_pok_data_rog": f'{data_rog}',
            "lekarsva_id": f'{id_lek}'
        }
def BaseLeuk(data, file_name):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def ShowLek(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return json.load(file)

def Per(str):
    try:
        int(str)
        return True
    except ValueError:
        return False