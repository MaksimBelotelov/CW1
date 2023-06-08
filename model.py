from datetime import date

class Memo:
    id_counter = 0

    def __init__(self, name: str, body: str):
        Memo.id_counter += 1
        self.id = Memo.id_counter
        self.name = name
        self.body = body
        self.date_of_change = date.today()

    def memo_to_str(self):
        return f'{self.id};{self.date_of_change};{self.name};{self.body}'

    def __str__(self):
        return f'{self.id:<3}{self.date_of_change}{self.name:<20}{self.body:<20}'

class Store:
    def __init__(self, path: str):
        self.path = path
        self.memo_store: list[Memo] = []