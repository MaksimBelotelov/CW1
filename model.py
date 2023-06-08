import csv
from datetime import date


class Memo:
    id_counter = 0

    def __init__(self, id: int, date_of_change: date, name: str, body: str):
        self.id = id
        self.name = name
        self.body = body
        self.date_of_change = date_of_change

    def get_id(self) -> int:
        return (int)(self.id)

    def memo_to_str(self):
        return f'{self.id};{self.date_of_change};{self.name};{self.body}'.strip()

    def __str__(self):
        return f'----------------------------------------------------------\n' \
               f'ID:{self.id:}\nДата:{self.date_of_change:}\nНазвание:{self.name:}\n' \
               f'{self.body}'

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
                if self.memo_store:
                    Memo.id_counter = self.memo_store[-1].id
        except FileNotFoundError:
            print('Ошибка! Файл с данными не найден!')

    def save(self):
            with open(self.path, "w", encoding = 'UTF-8') as csvfile:
                fieldnames = ['Id', 'Date', 'Name', 'Body']
                writer = csv.DictWriter(csvfile, delimiter= ';', fieldnames=fieldnames)
                writer.writeheader()
                for row in self.memo_store:
                    writer.writerow({'Id': row.id, 'Date': row.date_of_change, 'Name': row.name, 'Body': row.body})

    def add(self, new_note: Memo):
        self.memo_store.append(new_note)


