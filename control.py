from model import Per
from leuk_control import AddLeukatstvo, AddPostoyalLLa, EditLekar, Findskidka, DeleteLeuk, FindLeuk, ShowLek, DeleteSkidka, DeleteЗostoyal, FindSkidka, FindPostoyal, FindPostoyalLLa

def FuncEdit(skidka):
    print("1 - Изменить ID скидки")
    print("2 - Изменить процент скидки")
    print("3 - Изменить лейкарство")
    vibor = str(input("Выберите действие: "))
    if (Per(vibor) == True) and (1 <= int(vibor) <= 3):
        EditLekar(skidka, vibor)
    else:
        return FuncEdit(skidka)

def FuncStart(num):
    if num == "1":#Добавить лейкарство
        name = str(input("Ввведите название лейкарства: "))
        cost = str(input("Введите цену лейкарства: "))
        AddLeukatstvo(name, cost)
        return 'Лейкарство добавлено'

    elif num == "2":#Добавить постояльца
        fio = str(input("Ввведите ФИО постояльца: "))
        data_rog = str(input("Введите дату рождения "+fio+": "))
        id_lek = str(input("Введите ID лейкарства: "))
        AddPostoyalLLa(fio, data_rog, FindPostoyalLLa(id_lek))
        return 'Постоялец добавлен'

    elif num == "3":#Изменить скидку
        id = str(input("Введите ID скидки: "))
        FuncEdit(Findskidka(id))
        return 'Изменения сохранены'

    elif num == "4":#Удалить лейкарство
        naz_leuk = str(input("Введите ID лейкарства: "))
        print("Вы уверены, что хотите удалить лейкарство с ID "+naz_leuk)
        yber = str(input("Если да, то напишите УДАЛИТЬ: "))
        if yber == "УДАЛИТЬ":
            DeleteLeuk(FindLeuk(naz_leuk))
            DeleteSkidka(FindSkidka(naz_leuk))
            DeleteЗostoyal(FindPostoyal(naz_leuk))
            return 'Лейкарство удалено'

    elif num == "5":#Посмотреть БД, предлагает выбрать какую бд посмотреть
        print("Какую базу данных вы хотите посмотреть?")
        print("1 - Лейкарства")
        print("2 - Скидки")
        print("3 - Постоянные покупатели")
        print("4 - Поставщики")
        otvet = int(input("Выберите одну базу данных: "))
        if otvet == 1:
            lekar = ShowLek('bd.json')["lekarsva"]
            for i in range(len(lekar)):
                print(f'{lekar[i]}')
        elif otvet == 2:
            skid = ShowLek('bd.json')["skidka"]
            for i in range(len(skid)):
                print(f'{skid[i]}')
        elif otvet == 3:
            postoyal = ShowLek('bd.json')["postoyal_pok"]
            for i in range(len(postoyal)):
                print(f'{postoyal[i]}')
        elif otvet == 4:
            postavsh = ShowLek('bd.json')["postavshiki"]
            for i in range(len(postavsh)):
                print(f'{postavsh[i]}')
        else:
            print("Такой базы данных не существует! Попробуйте ещё раз.")
            FuncStart(num)