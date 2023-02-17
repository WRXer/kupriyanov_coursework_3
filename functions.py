import json
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
    operation.hiding_card()    #Скрываем частично номер карты
    for w in operation.finished_list:    #Выводим
        if 'перевод' in w['description'].lower():
            print(f"{w['date']} {w['description']}\n{w['from']} -> {w['to']}\n{w['operationAmount']['amount']} {w['operationAmount']['currency']['name']} \n ")
        else:
            print(f"{w['date']} {w['description']}\n{w['to']}\n{w['operationAmount']['amount']} {w['operationAmount']['currency']['name']} \n ")


