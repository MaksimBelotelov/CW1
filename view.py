from model import Memo, Store

def main_menu() -> int:
    ch = ''
    while True:
        print('''        Главное меню:
--------------------------------        
1. Показать список всех заметок
2. Просмотреть заметку
3. Создать новую заметку
4. Редактировать заметку
5. Сохранить изменения
6. Удалить заметку
7. Выход
--------------------------------''')
        ch = input()
        if ch.isdigit() and 0 < int(ch) < 8:
            ch = (int)(ch)
            return ch
        else:
            print('Необходимо ввести цифру от 1 до 7')

def show_me_all_notes(store: Store):
    if store.get_memo_store():
        for item in store.get_memo_store():
            print(item)
    else:
        print('Список заметок пуст.')