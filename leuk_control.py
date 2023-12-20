from model import Leuk, ShowLek, BaseLeuk, Postoyal
def AddLeukatstvo(name, cost):
    base = ShowLek('bd.json')
    id = get_all()[-1]["lekarsva_id"]
    leukar = Leuk(str(int(id)+1),name, cost)
    base["lekarsva"].append(leukar.data)
    BaseLeuk(base, 'bd.json')

def AddPostoyalLLa(fio, data_rog, id_lek):
    base = ShowLek('bd.json')
    id = get_allpost()[-1]["postoyal_pok_id"]
    postoyal_pokyp = Postoyal(str(int(id)+1), fio, data_rog, id_lek)
    base["postoyal_pok"].append(postoyal_pokyp.data)
    BaseLeuk(base, 'bd.json')

def FindPostoyalLLa(id_lek):
    try:
        chetchik = 0
        base = ShowLek('bd.json')
        for postoyal in base["postoyal_pok"]:
            if postoyal["lekarsva_id"] == id_lek:
                chetchik +=1
                return postoyal["lekarsva_id"]
        if chetchik == 0:
            int('a')
    except:
        print('Такого лейкарства не найдено. Попробуйте еще раз!')
        id_lek = str(input("Введите ID скидки: "))
        return FindPostoyalLLa(id_lek)
def get_all():
    db = ShowLek('bd.json')
    return db["lekarsva"]
def get_allpost():
    db = ShowLek('bd.json')
    return db["postoyal_pok"]
def Findskidka(skid):
    try:
        chetchik = 0
        base = ShowLek('bd.json')
        for skidka in base["skidka"]:
            if skidka["skidki_id"] == skid:
                chetchik +=1
                return skidka
        if chetchik == 0:
            int('a')
    except:
        print('Такой скидки не найдено. Попробуйте еще раз!')
        skid = str(input("Введите ID скидки: "))
        return Findskidka(skid)

def FindLeuk(naz_leuk):
    try:
        counter = 0
        base = ShowLek('bd.json')
        for lek in base["lekarsva"]:
            if lek["lekarsva_id"] == naz_leuk:
                counter +=1
                return lek
        if counter == 0:
            int('a')
    except:
        print('Такого лейкарства не найдено. Попробуйте еще раз!')
        naz_leuk = str(input("Введите ID лейкарства: "))
        return FindLeuk(naz_leuk)

def FindSkidka(naz_leuk):
    try:
        counter = 0
        base = ShowLek('bd.json')
        for lek in base["skidka"]:
            if lek["lekarsva_id"] == naz_leuk:
                counter +=1
                return lek
        if counter == 0:
            int('a')
    except:
        print('Такого лейкарства не найдено. Попробуйте еще раз!')
        naz_leuk = str(input("Введите название лейкарства: "))
        return FindLeuk(naz_leuk)
def FindPostoyal(naz_leuk):
    try:
        counter = 0
        base = ShowLek('bd.json')
        for lek in base["postoyal_pok"]:
            if lek["lekarsva_id"] == naz_leuk:
                counter +=1
                return lek
        if counter == 0:
            int('a')
    except:
        print('Такого лейкарства не найдено. Попробуйте еще раз!')
        naz_leuk = str(input("Введите название лейкарства: "))
        return FindLeuk(naz_leuk)
def DeleteLeuk(leuk):
    string = 0
    base = ShowLek('bd.json')
    for step in range(0,len(base['lekarsva'])):
        if leuk == base['lekarsva'][string]:
            del base['lekarsva'][string]
        else:
            string += 1
    BaseLeuk(base, 'bd.json')
def DeleteSkidka(leuk):
    string = 0
    base = ShowLek('bd.json')
    for step in range(0,len(base['skidka'])):
        if leuk == base['skidka'][string]:
            del base['skidka'][string]
        else:
            string += 1
    BaseLeuk(base, 'bd.json')
def DeleteЗostoyal(leuk):
    string = 0
    base = ShowLek('bd.json')
    for step in range(0,len(base['postoyal_pok'])):
        if leuk == base['postoyal_pok'][string]:
            del base['postoyal_pok'][string]
        else:
            string += 1
    BaseLeuk(base, 'bd.json')

def EditLekar(skidka, number_step):
    chetchik = 0
    base = ShowLek('bd.json')
    for base_student in base['skidka']:
        chetchik += 1
        if base_student == skidka:
            if int(number_step) == 1:
                new_id = str(input("Введите новое ID: "))
                base['skidka'][chetchik-1]['skidki_id'] = new_id
                BaseLeuk(base, 'bd.json')
            if int(number_step) == 2:
                new_proLL = str(input("Введите новый процент: "))
                base['skidka'][chetchik-1]['skidki_proLL'] = new_proLL
                BaseLeuk(base, 'bd.json')
            if int(number_step) == 3:
                new_name = str(input("Введите новое лейкарство: "))
                base['skidka'][chetchik-1]['lekarsva_name'] = new_name
                BaseLeuk(base, 'bd.json')