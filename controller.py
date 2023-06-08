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
                notes.add(view.create_new_note(notes))
            case 4:
                view.show_me_all_notes(notes)
                view.edit_note(notes)
            case 5:
                notes.save()
            case 6:
                notes.remove(view.remove_note())
                print('Заметка удалена.')
            case 7:
                if view.save_before_exit():
                    notes.save()
                exit(0)