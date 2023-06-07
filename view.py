import text as t

def main_menu() -> int:
    ch = ''
    while True:
        print(t.main_menu)
        ch = input()
        if ch.isdigit() and 0 < int(ch) < 8:
            ch = (int)(ch)
            return ch
        else:
            print('Необходимо ввести цифру от 1 до 7')