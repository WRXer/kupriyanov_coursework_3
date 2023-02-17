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


def main():
    operation = load_words()    #Загружаем бд
    operation.sorted_date()    #Сортируем по дате
    operation.last_operations()    #Находим последние 5 операций
    operation.finish_list()    #Готовим к выводу


