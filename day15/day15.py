
def get_input():
    f = open("input", "r")
    lines = f.read()
    input_data = lines.strip().split(',')
    f.close()
    return input_data

def read_starting_numbers(data):
    starting_numbers = {}
    for i in range(len(data)):
        starting_numbers[int(data[i])] = (0, i+1)
    return starting_numbers

def solve(input_data, target_num):
    numbers = read_starting_numbers(input_data)
    input_data_length = len(input_data)
    counter = input_data_length + 1
    spoken_num = input_data[input_data_length-1]

    while(counter <= target_num):
        if numbers.get(spoken_num) is not None:
            num = numbers.get(spoken_num)
            if num[0] != 0 and num[1] != 0:
                spoken_num = num[1]-num[0]
                if numbers.get(spoken_num) is not None:
                    num = numbers.get(spoken_num)
                    numbers[spoken_num] = (num[1], counter)
                else:
                    numbers[spoken_num] = (0, counter)
            else:
                spoken_num = 0
                num = numbers.get(spoken_num)
                numbers[spoken_num] = (num[1], counter)
            counter+=1
        else:
            if numbers.get(0) is not None:
                num = numbers.get(0)
                numbers[0] = (num[1], counter)
                spoken_num = 0
            else:
                numbers[0] = (0, counter)
                spoken_num = 0
            counter+=1
    print("Spoken number at round", counter-1,":", spoken_num)

if __name__ == "__main__":
    input_data = get_input()
    solve(input_data, 2020)
    solve(input_data, 30000000)

