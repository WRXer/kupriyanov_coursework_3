import json
from _datetime import datetime


def load_words():
    """
    Функция преобразования файла из джсон
    """
    with open('operations.json', 'r', encoding='utf-8') as file:
        raw_json = file.read()
        words = json.loads(raw_json)
        return words


def user_id():
    """
    Функция проверки правильного ввода айди клиента
    """
    while True:
        #user_input = input("Введите айди пользователя")   #Открыть при сдаче
        user_input = '587085106'
        if user_input.isdigit():
            return user_input
            break
        else:
            print("Введите айди в цифровом формате!")
            continue


def one_user_story(words,user,count):
    """
    Функция загрузки данных одного пользователя
    """
    one_user_story = []
    for w in words:
        if int(user) == w["id"]:
            count +=1
            one_user_story.append(w)
            return one_user_story,count
        else:
            continue


def sorted_date(words):
    """
    Функция сортировке по дате(сверху самые последние)
    """
    my_dict = {}
    for w in words:
        if not w:    #Ищем пустые словари
            continue
        else:
            if w['state'].lower() == "executed":    #Условие, что операция выполнена
                y = []
                c = 0
                for i in w['date']:
                    if i.isdigit() and c < 12:
                        y.append(i)
                        c +=1
                    else:
                        continue
                w['data'] = int("".join(y))
                my_dict[w['id']] = w['data']
            else:
                continue
    return dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))


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
    words = load_words()  # Загружаем бд
    sorted_date_d = sorted_date(words)
    l_o = last_operations(sorted_date_d)  # Last operations