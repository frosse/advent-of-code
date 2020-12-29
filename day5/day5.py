import math

def get_input():
    f = open("input", "r")
    return [line.strip() for line in f.readlines()]


def solve():
    data = get_input()
    highest = 0
    ids = set()
    for line in data:
        min = 0
        max = 127
        mid = max//2
        col_min = 0
        col_max = 7
        col_mid = col_max //2
        result = 0
        for c in line:
            if c == 'B':
                min = mid+1
                mid = math.floor(max - (max - min) / 2)
            if c == 'F':
                max = mid
                mid = math.floor(max - (max - min) / 2)
            if c == 'R':
                col_min = col_mid+1
                col_mid = math.floor(col_max - (col_max - col_min) / 2)
            if c == 'L':
                col_max = col_mid
                col_mid = math.floor(col_max - (col_max - col_min) / 2)

        result = mid * 8 + col_mid
        if result > highest:
            highest = result
        ids.add(result)
    print("Highest seat ID:", highest)

    my_seat = 0
    for id in ids:
        if id+1 not in ids:
            my_seat = id+1
            break
    print("My seat ID:", my_seat)


if __name__ == '__main__':
    solve()
