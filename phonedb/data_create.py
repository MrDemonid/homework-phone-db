def input_user_data():
    name = input("Введите имя: ")
    surname = input("Введите фамилия: ")
    phone = input("Введите телефон: ")
    adress = input("Введите адрес: ")
    return name, surname, phone, adress

def input_menu(menustr, vars):
    print(menustr)
    while True:
        res = input('Ваш выбор => ')
        if res.lower() in vars:
            break
    return res.lower()

