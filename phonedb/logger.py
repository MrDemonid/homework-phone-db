from data_create import input_user_data, input_menu
from file_io import *



svar1 = "{}\n{}\n{}\n{}\n"
svar2 = "{};{};{};{}\n"
svars = [svar1, svar2]


'''
    Добавляет запись в один из файлов
'''
def input_data():
    name, surname, phone, adress = input_user_data()
    var = int(select_format('В каком формате сохранить данные?', name, surname, phone, adress))
    if var > 0:
        frm = svars[var-1]
        fio_append(var, frm.format(name, surname, phone, adress)+'\n')
    
""" 
    Вывод данных из файлов *.csv
"""
def print_data():
    print('--------- данные ---------')
    print('1 файл:')
    lst = fio_load_first()
    for i in lst:
        print(i)
    print('2 файл:')
    lst = fio_load_second()
    for i in lst:
        print(i)

'''
    Копирует запись с одного файла в другой
'''
def copy_data():
    var = int(select_format('Выберите исходный формат данных'))
    if var > 0:
        rec = select_rec(var)
        if len(rec) > 0:
            if var == 1:
                dest = 2
                res = rec.replace("\n",";") + "\n\n"
            elif var == 2:
                dest = 1
                res = rec.replace(";","\n") + "\n"
            fio_append(dest, res)
            print('Данные успешно скопированы.')

'''
    Удаляет запись из файла
'''
def delete_data():
    var = int(select_format('Из какого формата удалить данные?'))
    if var > 0:
        rec, lst = select_numrec(var)
        if rec > 0:
            lst.pop(rec-1)
            fio_rewrite(var, lst)
            print('Данные успешно удалены.')        

'''
    Изменяет запись в файле
'''
def change_data():
    var = int(select_format('В каком формате изменить данные?'))
    if var > 0:
        rec, lst = select_numrec(var)
        if rec > 0:
            print('Исходные данные:')
            print(lst[rec-1])
            print('Введите новые данные:')
            name, surname, phone, adress = input_user_data()
            res = svars[var-1].format(name, surname, phone, adress)
            lst.pop(rec-1)
            lst.insert(rec-1, res)
            fio_rewrite(var, lst)
            print('Данные успешно изменены.')

'''
    поиск данных по фамилии или телефону
'''
def find_data():
    print("Введите любые данные, по которым искать:")
    name, surname, phone, adress = input_user_data()
    if len(name) == 0 and len(surname) == 0 and len(phone) == 0 and len(adress) == 0:
        return
    print('Ищем...\n')
    lst = fio_load_first()
    for i in lst:
        if compare_rec(name, surname, phone, adress, i):
            print(i)
            
    lst = fio_load_second()
    for i in lst:
        if compare_rec(name, surname, phone, adress, i):
            print(i)
    print('Поиск закончен')
    

'''
    сравнивает запись rec с данными имени, телефона и адреса
'''
def compare_rec(name, surname, phone, adress, rec):
    data = rec.split('\n')
    if len(data) < 4:
        # пробуем разделить по ';'
        data = data[0].split(';')           # в data[0] у нас исходная строка, но без завершающего '\n'          
        if len(data) < 4:
            return False
    if len(name) > 0 and name != data[0]:
            return False
    if len(surname) > 0 and surname != data[1]:
        return False
    if len(phone) > 0 and phone != data[2]:
        return False
    if len(adress) > 0 and adress != data[3]:
        return False
    return True



'''
    выбор типа представления данных
'''
def select_format(menustr, name='name', surname='surname', phone='phone', adress='address'):
    var = input_menu(f'{menustr}\n'
            f'1) Вариант:\n'
            f'{svar1.format(name, surname, phone, adress)}'
            f'2) Вариант:\n'
            f'{svar2.format(name, surname, phone, adress)}'
            '0) Отмена\n',
            (['1', '2', '0']))
    return var

'''
    показ нумерованного списка и выбор записи
    на входе: номер варианта (first or second)
    на выходе: строка (выбранная запись) или пустая строка (ошибка)
'''
def select_rec(variant):
    rec, lst = select_numrec(variant)
    if rec > 0:
        return lst[rec-1]
    return ""

'''
    Выбор номера записи в файле, в случае отмены (или пустого файла) вернёт 0 и ""
'''
def select_numrec(variant):
    if variant == 1:
        lst = fio_load_first()
    elif variant == 2:
        lst = fio_load_second()
    else:
        return ''
    print('Выберете номер записи:')
    for i in range(0, len(lst)):
        print(i+1,') ', lst[i])
    print('0) Отмена')
    rec = int(input_menu('\n', [str(x) for x in range(len(lst)+1)]))
    return rec, lst
