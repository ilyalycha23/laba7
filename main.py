from model import Per
from control import FuncStart

def Main():
    print("1 - Добавить лейкарство")
    print("2 - Добавить постояльца")
    print("3 - Изменить скидку")
    print("4 - Удалить лейкарство")
    print("5 - Посмотреть базы данных")
    otvet = str(input("Выберите действие: "))
    if (Per(otvet) == True) and (1 <= int(otvet) <= 5):
        return FuncStart(otvet)
    else:
        Main()

print(Main())

'''
Связь:
При удалении "лейкарства" из базы данных Лейкарство, 
автоматически удаляется "скидка" и "постояльцы" на это лейкарство
'''