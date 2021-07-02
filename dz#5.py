import pickle
from itertools import zip_longest


def read_file(us, hob, res):
    user = []
    hobb = []
    with open(us, 'r') as users:
        for line in users:
            user.append(tuple(line.replace('\n', '').split(',')))

    with open(hob, 'r') as hobby:
        for line in hobby:
            hobb.append(tuple(line.replace('\n', '').split(',')))

    if len(hobb) > len(user):
        return 1

    result_user_hobb = dict(zip_longest(user, hobb, fillvalue=None))
    print(result_user_hobb)

    with open(res, 'wb') as users_hobby:
        pickle.dump(result_user_hobb, users_hobby)

    with open(res, 'rb') as users_hobby:
        users_hobbie = pickle.load(users_hobby)

    print(users_hobbie)
if __name__ == '__main__':
    users_file = input('csv file for users: ')
    hobby_file = input('csv file for hobby: ')
    res_file = input('csv file for res: ')
    read_file(users_file, hobby_file, res_file)