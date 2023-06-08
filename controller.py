import view
from model import Memo, Store


def start():
    notes = Store('Notes.csv')
    notes.open()

    while True:
        user_choice = view.main_menu()
        match user_choice:
            case 1:
                view.show_me_all_notes(notes)
            case 2:
                view.show_me_all_notes(notes)
                index = input('Введите номер заметки, которую хотите открыть:')
                if(index.isdigit()):
                    view.show_me_this_note((int)(index), notes)
                else:
                    print('Необходимо ввести Id записи')
            case 3:
                break
            case 4:
                break
            case 5:
                break
            case 6:
                notes.save()
            case 7:
                exit(0)