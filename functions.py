import json
from _datetime import datetime
from operations import Operations

def load_words():
    """
    Функция преобразования файла из джсон
    """
    with open('operations.json', 'r', encoding='utf-8') as file:
        raw_json = file.read()
        words = json.loads(raw_json)
        return Operations(words=words)


def last_operations(sorted_date_d):
    """
    Функция определения последних 5 операций
    """
    count = 0
    l_o = {}
    for k,v in sorted_date_d.items():
        if count < 5:
            count += 1
            l_o[k] = v
    return l_o


def finish_list(words, l_o):
    """
    Окончательный список
    """
    finish_list = []
    for l in l_o.keys():
        for w in words:
            if not w:  # Ищем пустые словари
                continue
            else:
                if l == w['id']:
                    finish_list.append(w)
                else:
                    continue
    return finish_list


def main():
    operation = load_words()  # Загружаем бд
    operation.sorted_date()
    operation.last_operations()

