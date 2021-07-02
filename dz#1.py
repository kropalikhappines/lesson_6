
def read_file():
    result = []
    with open('nginx_logs.txt', 'r', encoding='utf-8') as log_file:
        for line in log_file:
            line = line.replace('"', '').replace('-', '')
            lst_line = line.split()
            result.append((lst_line[0], lst_line[3], lst_line[4]))

    return result



print(read_file())
