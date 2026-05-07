# DEFINICJA PROSTEJ STRUKTORY DANYCH OBEJMUJACEJ PROSTEGO UZRYTKOWNIKA
from mapbook_lib.model import users
from mapbook_lib.controler import *


def main():
    while True:
        print('==========MENU==============')
        print('0 - Koniec')
        print('1 - Wyświetl znajomych')
        print('2 - Dodanie znajomych')
        print('3 - Usuń znajomego')
        print('4 - Zaktualizuj użytkownika')
        print('5 - Zaktualizuj posta użytkownika')
        choice = input('Wybierz opcję:\t')
        print(f'Wybrano opcję {choice}')
        if choice == '0':
            break
        if choice == '1':
            read_users(users)
        if choice == '2':
            add_user(users)
        if choice == '3':
            remove_user(users)
        if choice == '4':
            update_user(users)
        if choice == '5':
            update_user_post(users)

if __name__ == '__main__':
    main()