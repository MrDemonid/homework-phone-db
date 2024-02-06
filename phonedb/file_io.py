
def fio_get_first_name():
    return 'data_first_variant.csv'

def fio_get_second_name():
    return 'data_second_variant.csv'

def fio_get_file_name(var):
    if var == 1:
        return fio_get_first_name()
    elif var == 2:
        return fio_get_second_name()
    return ""


'''
    подгружает данные из первого типа файла и возвращает список строк
'''
def fio_load_first():
    with open(fio_get_first_name(), 'r', encoding='utf-8') as file:
        res = []
        data = file.readlines()
        datalen = (len(data) // 5) * 5      # данные должны быть по 5 строк
        for i in range (0, datalen, 5):
            item = data[i] + data[i+1] + data[i+2] + data[i+3]  # последний перевод строки не нужен
            res.append(item)
    if datalen != len(data):
        fio_rewrite(1, res)                 # корректируем файл
    return res

'''
    подгружает данные из второго типа файла и возвращает список строк
'''
def fio_load_second():
    with open(fio_get_second_name(), 'r', encoding='utf-8') as file:
        is_bad = False
        res = []
        data = file.readlines()
        for i in range(0, len(data)):
            item = data[i]
            if (i & 1) == 1:                # нечётные строки должны быть пустыми
                if item != '\n':
                    is_bad = True
            if item != '\n':                # лишние переводы строк опускаем
                res.append(item)
        if is_bad:
            fio_rewrite(2, res)             # корректируем файл
    return res        


'''
    добавляет данные в файл
    на входе: номер варианта
'''
def fio_append(var, string):
    fname = fio_get_file_name(var)
    if len(fname) == 0:
        return
    with open(fname, 'a', encoding='utf-8') as file:
        file.write(string)

'''
    полностью перезаписывает файл
    на входе: номер варианта и список данных
'''
def fio_rewrite(var, lst):
    fname = fio_get_file_name(var)
    if len(fname) == 0:
        return
    with open(fname, 'w', encoding='utf-8') as file:
        for i in lst:
            file.write(f'{i}\n')
 