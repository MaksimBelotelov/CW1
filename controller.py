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
                break
            case 3:
                break
            case 4:
                break
            case 5:
                break
            case 6:
                break
            case 7:
                exit(0)