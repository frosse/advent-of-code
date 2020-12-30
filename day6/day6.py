
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


def solve_part_two():
    data = get_input()
    answers = {}
    result = 0
    counter = 0
    for line in data:
        if line == '':
            old_result = result
            for val in answers.values():
                if val == counter:
                    result += 1
            answers = {}
            counter = 0
        else:
            counter += 1
        for c in line:
            if c in answers:
                answers[c] += 1
            else:
                answers[c] = 1
    print(result)


if __name__ == '__main__':
    solve()
    solve_part_two()
