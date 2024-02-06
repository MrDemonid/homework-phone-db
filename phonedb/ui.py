""" 
Бот телефонной книги.
"""
from logger import input_data, print_data, copy_data, delete_data, change_data, find_data
from data_create import input_menu


def interface():
    while True:
    
        print()
        
        command = input_menu('\n------------------------\n'
            'Добрый день! Это бот-помощник.\n'
            'Что вы хотите сделать? \n'
            '1) - Записать данные \n'
            '2) - Вывести данные\n'
            '3) - Копировать данные\n'
            '4) - Удалить данные\n'
            '5) - Изменить данные\n'
            '6) - Найти данные\n'
            'exit - Выход\n',
            ['1', '2', '3', '4', '5', '6', 'exit'])
        
        if command == '1':
            input_data()
        elif command == '2':
            print_data()
        elif command == '3':
            copy_data()
        elif command == '4':
            delete_data()
        elif command == '5':
            change_data()
        elif command == '6':
            find_data()
        else:
            break


interface()
