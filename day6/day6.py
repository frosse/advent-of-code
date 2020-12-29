
def get_input():
    f = open("input", "r")
    return [line.strip() for line in f.readlines()]


def solve():
    data = get_input()
    answers = set()
    result = 0
    for line in data:
        if line == '':
            result += len(answers)
            answers = set()
        for c in line:
            answers.add(c)
    print(result)


if __name__ == '__main__':
    solve()
