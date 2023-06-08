import csv
from datetime import date

class Memo:
    id_counter = 0

    def __init__(self, id: int, date_of_change: date, name: str, body: str):
        self.id = id
        self.name = name
        self.body = body
        self.date_of_change = date_of_change

    def memo_to_str(self):
        return f'{self.id};{self.date_of_change};{self.name};{self.body}'

    def __str__(self):
        return f'{self.id:<2}{self.date_of_change:<11}{self.name:<20}'

class Store:
    def __init__(self, path: str):
        self.path = path
        self.memo_store: list[Memo] = []

    def get_memo_store(self):
        return self.memo_store

    def open(self):
        self.memo_store.clear()
        try:
            with open(self.path, encoding = 'UTF-8') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=';')
                for row in reader:
                    self.memo_store.append(Memo(row['Id'], row['Date'], row['Name'], row['Body']))
        except FileNotFoundError:
            print('Ошибка! Файл с данными не найден!')

