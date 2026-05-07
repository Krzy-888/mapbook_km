# DEFINICJA PROSTEJ STRUKTORY DANYCH OBEJMUJACEJ PROSTEGO UZRYTKOWNIKA
from os import remove

users = [{"username": 'Artur',
          "Location": 'Warszawa',
          "Posts": ['Sprzedam Mercedesa', 'Kupię skrzynię biegów', 'Ratunku co robić po wypadku',
                    'Kto dziś idzie biegać']},
         {"username": 'Daniel',
          "Location": 'Legionowo',
          "Posts": ['', '', 'mój kod nie działa pomocy!']},
         {"username": 'Kamil',
          "Location": 'Ciechanów',
          "Posts": ['', '', 'Czy ktoś zrobił już sprawozdanie z PPyt']
          }]


def read_users(users_data: list) -> None:
    for user in users_data:
        print(
            f'Twój znajomy {user["username"]}, z miejscowosci {user["Location"]}, opublikował posta {user["Posts"][-1]}')


def add_user(users_data: list) -> None:
    users_data.append({"username": input('enter user name:\t'),
                       "Location": input('enter location:\t'),
                       "Posts": ['Dołączyłem do Systemu']
                       })


def remove_user(users_data: list) -> None:
    name2remove = input('enter user name:\t')
    for user in users_data:
        if user['username'] == name2remove:
            users.remove(user)


def update_user(users_data: list) -> None:
    name2update = input('enter user name:\t')
    for user in users_data:
        if user['username'] == name2update:
            user['username'] = input('enter new name:\t')
            user['Location'] = input('enter new location:\t')

def update_user_post(users_data: list) -> None:
    name2update = input('enter user name:\t')
    for user in users_data:
        if user['username'] == name2update:
            user['Posts'].append(input('enter new Post:\t'))

while True:
    print('==========MENU==============')
    print('0 - Koniec')
    print('1 - Wyświetl znajomych')
    print('2 - Dodanie znajomych')
    print('3 - Usuń znajomego')
    print('4 - Zaktualizuj użytkownika')
    print('5 - Zaktualizuj posta użytkownika')
    Choice = input('Wybierz opcję:\t')
    print(f'Wybrano opcję {Choice}')
    if Choice == '0':
        break
    if Choice == '1':
        read_users(users)
    if Choice == '2':
        add_user(users)
    if Choice == '3':
        remove_user(users)
    if Choice == '4':
        update_user(users)
    if Choice == '5':
        update_user_post(users)