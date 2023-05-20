import json
import os.path
from datetime import datetime

a = os.path.join('../operations.json')


def load_data():
    """ выгружаем файлы из json"""
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.loads(file.read())
    return data


def sorted_operation(data):
    """
    сортирует по дате
    """
    new_data = []
    for el in data:
        if 'date' in el:
            new_data.append(el)
    return sorted(new_data, key=lambda d: d['date'])[-5:]




def status_operations(spisok):
    '''отбирает операции в статусе EXECUTED'''
    data = []
    for i in spisok:
        if i['state'] == 'EXECUTED':
            data.append(i)
            if len(data) == 5:
                break
    return data


def masked_card_from(spisok):
    """
Функция маскирующая цифры в номере карты и счете
"""
    for i in spisok:
        try:

            number = i['from'].split()[-1]
            if len(number) == 16:
                i['from'] = number[:4] + " " + number[4:6] + "** **** " + number[-4:]

            else:
                i['from'] = "**" + number[-4:]
        except KeyError: pass
    return spisok


def masked_account_from(spisok):
    """
Функция маскирующая цифры в номере карты и счете
    """
    for i in spisok:
        try:

            number = i['to'].split()[-1]
            if len(number) == 16:
                i['to'] = number[:4] + " " + number[4:6] + "** ****" + number[-4:]
            else:
                i['to'] = "**" + number[-4:]
        except KeyError: pass
    return spisok


def change_date(spisok):
    """Метод изменяет дату на ту которая нужна нам"""
    for i in spisok:
        i['date'] = datetime.strptime(i['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d %m %Y')
    return spisok
