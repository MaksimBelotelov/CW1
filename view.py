from model import Memo, Store
from datetime import date


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
            ch = int(ch)
            return ch
        else:
            print('Необходимо ввести цифру от 1 до 7')


def show_me_all_notes(store: Store):
    if store.get_memo_store():
        for item in store.get_memo_store():
            print(f'{item.id:<2}{item.date_of_change} {item.name:<20}')
    else:
        print('Список заметок пуст.')


def show_me_this_note(id: int, store: Store):
    if store.get_memo_store():
        for item in store.get_memo_store():
            if item.get_id() == id:
                print(item)
                return
    print('В списке нет заметки с таким номером.')


def create_new_note(store: Store) -> Memo:
    name = input('Введите название для заметки: ')
    print('Введите заметку. Для окончания введите пустую строку.')
    body = ""
    while True:
        s = input()
        if s:
            body += s + '\n'
        else:
            break
    Memo.id_counter = int(Memo.id_counter) + 1
    return Memo(Memo.id_counter, date.today(), name, body)


def remove_note() -> int:
    id_to_remove = int(input('Введите id заметки, которую вы хотите удалить: '))
    return id_to_remove


def edit_note(store: Store):
    id_to_edit = int(input('Введите id заметки, которую вы хотите изменить: '))
    if store.get_memo_store():
        for item in store.get_memo_store():
            if item.get_id() == id_to_edit:
                answer = input(f'Текущее название заметки:\n {item.name}\n Изменить его? (y/n): ')
                if answer == 'y' or answer == 'Y':
                    item.name = input("Введите новое название для заметки: ")
                answer = input(f'Текущее содержание заметки:\n{item.body}\n Изменить его? (y/n): ')
                if answer == 'y' or answer == 'Y':
                    print("Введите новое содержание заметки: ")
                    item.body = ""
                    while True:
                        s = input()
                        if s:
                            item.body += s + '\n'
                        else:
                            break
                return
    print('В списке нет заметки с таким номером.')

def save_before_exit() -> bool:
    answer = input('Сохранить внесенные изменения? (y/n): ')
    return answer == 'y' or answer == 'Y'