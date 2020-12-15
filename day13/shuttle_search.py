
def get_input(input):
    f = open(input, "r")
    return [line for line in f.readlines()]


def solve_part_one(input):
    data = get_input(input)
    timestamp = data[0]
    busses = []
    for d in data[1].split(','):
        if d != "x":
            tmp = int(d)
            busses.append(tmp)
        else:
            pass

    results = []
    for bus in busses:
        time = bus
        while(time <= int(timestamp)):
            time = time + bus
        results.append(time)

    for result in results:
        if result > int(timestamp):
            print(result - int(timestamp))

def solve_part_two(input):
    data = get_input(input)
    data2 = data[1].strip()
    busses = []
    for d in data2.split(","):
        if d != ",":
            busses.append(d)
    bus_dict = {
            }
    counter = 0
    bus_list = []
    for bus in busses:
        if bus != "x":
            bus_list.append((int(bus), counter))
            counter += 1
        else:
            counter += 1
    bus_list = sorted(bus_list, reverse=True)
    result = []
    time = bus_list[0][0] - bus_list[0][1]
    increment = bus_list[0][0]
    counter = 1
    result.append(bus_list[0][0])
    while True:
        if (time + bus_list[counter][1]) % bus_list[counter][0] != 0:
            time += increment
        else:
            result.append(bus_list[counter][0])
            increment = get_value(result)
            counter += 1
        if len(result) == len(bus_list):
            print(time)
            break

def get_value(result):
    r = 1
    for i in result:
        r = r * i
    return r

if __name__ == "__main__":
    solve_part_one("input")
    solve_part_two("input")
