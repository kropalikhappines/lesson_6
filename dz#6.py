import sys

def append_sale(num):
    with open('bakery.csv', 'a', encoding='utf-8') as bakery_file:
        bakery_file.write(num + '\n')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        value = sys.argv[1]
        append_sale(value)
    else:
        print('no arg')