from collections import defaultdict


def read_file():
    result = {}
    count = defaultdict(int)
    with open('nginx_logs.txt', 'r', encoding='utf-8') as log_file:
        for line in log_file:
            line = line.replace('"', '').replace('-', '')
            lst_line = line.split()
            result[lst_line[0]] = (lst_line[0], lst_line[3], lst_line[4])

            count[lst_line[0]] += 1

    sorted_count = sorted(count.items(), key=lambda item:item[1])
    spammer = sorted_count[-1]
    return spammer
print(read_file())
