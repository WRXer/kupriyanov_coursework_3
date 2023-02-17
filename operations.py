from _datetime import datetime


class Operations():
    def __init__(self, words):
        self.words = words

        self.sorted_to_dates = None
        self.last_five_operations = None
        self.finished_list = None


    def sorted_date(self):
        """
        Функция сортировки по дате(сверху самые последние)
        """
        my_dict = {}
        for w in self.words:
            if not w:  # Ищем пустые словари
                continue
            else:
                if w['state'].lower() == "executed":  # Условие, что операция выполнена
                    y = []
                    c = 0
                    for i in w['date']:
                        if i.isdigit() and c < 12:
                            y.append(i)
                            c += 1
                        else:
                            continue
                    w['data'] = int("".join(y))
                    my_dict[w['id']] = w['data']
                else:
                    continue
        self.sorted_to_dates = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
        return self.sorted_to_dates


    def last_operations(self):
        """
        Функция определения последних 5 операций
        """
        count = 0
        self.last_five_operations = {}
        for key,value in self.sorted_to_dates.items():
            if count < 5:
                self.last_five_operations[key] = value
                count += 1
        return self.last_five_operations


    def finish_list(self):
        """
        Окончательный список
        """
        self.finished_list = []
        for l in self.last_five_operations.keys():
            for w in self.words:
                if not w:  # Ищем пустые словари
                    continue
                else:
                    if l == w['id']:
                        self.finished_list.append(w)
                    else:
                        continue
        return self.finished_list


    def hiding_card(self):
        """
        Частичное скрытие карты и счета
        """
        for k in self.finished_list:
            if 'перевод' in k['description'].lower():
                str = k['from']    #Скрываем номер карты отправителя
                strlength = len(str)
                masked = strlength - 4
                start_str = str[:masked - 6]
                end_str = str[masked:]
                mask_from = start_str + "*" * 6 + end_str
                str = k['to']    #Скрываем номер карты получателя
                strlength = len(str)
                masked = strlength - 4
                slimstr = str[masked:]
                mask_to = "*" * 2 + slimstr
                k['from'] = mask_from
                k['to'] = mask_to
                dt = datetime.strptime(k['date'], "%Y-%m-%dT%H:%M:%S.%f")    #Делаем сокращенным время
                new_format = dt.strftime("%d.%m.%Y")
                k['date'] = new_format
            else:
                str = k['to']    #Скрываем номер карты получателя
                strlength = len(str)
                masked = strlength - 4
                start_str = str[:masked - 16]
                end_str = str[masked:]
                mask_to = start_str + "*" * 2 + end_str
                k['to'] = mask_to
                dt = datetime.strptime(k['date'], "%Y-%m-%dT%H:%M:%S.%f")    #Делаем сокращенным время
                new_format = dt.strftime("%d.%m.%Y")
                k['date'] = new_format
        return self.finished_list
