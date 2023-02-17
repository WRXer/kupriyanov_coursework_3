class Operations():
    def __init__(self, words):
        self.words = words

        self.sorted_to_dates = None
        self.last_f_operations = None

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