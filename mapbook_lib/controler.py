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
            users_data.remove(user)


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
