import sys
from itertools import islice

def show_sale(from_b=None, to_b=None):
    with open('bakery.csv', 'r', encoding='utf-8') as bakery:
        if not from_b and not to_b:
            for line in bakery:
                print(line.replace('\n', ''))
        if from_b and to_b:
            for line in islice(bakery, from_b - 1, to_b - 1 + 1):
                print(line.replace('\n', ''))
        if from_b and not to_b:
            for line in islice(bakery, from_b - 1, None):
                print(line.replace('\n', ''))

if __name__ == '__main__':
    from_b = None
    to_b = None
    if len(sys.argv) == 2:
        from_b = int(sys.argv[1])
    elif len(sys.argv) == 3:
        from_b = int(sys.argv[1])
        to_b = int(sys.argv[2])
    show_sale(from_b, to_b)