import pickle
from itertools import zip_longest


def read_file():
    user = []
    hobb = []
    with open('users.csv', 'r', encoding='utf-8') as users:
        for line in users:
            user.append(line.replace('\n', '').replace(',', ' '))

    with open('hobby.csv', 'r', encoding='utf-8') as hobby:
        for line in hobby:
            hobb.append(line.replace('\n', ''))

    if len(hobb) > len(user):
        return 1

    result_user_hobb = dict(zip_longest(user, hobb, fillvalue=None))
    print(result_user_hobb)

    with open('users_hobby_file.csv', 'wb') as users_hobby:
        pickle.dump(result_user_hobb, users_hobby)

    with open('users_hobby_file.csv', 'rb') as users_hobby:
        users_hobbie = pickle.load(users_hobby)

    print(users_hobbie)
read_file()