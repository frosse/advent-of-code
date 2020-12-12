
def move(direction, pos, line):
    if direction == 'N':
        pos = (pos[0]+int(line[1:]), pos[1])
    if direction == 'S':
        pos = (pos[0]-int(line[1:]), pos[1])
    if direction == 'E':
        pos = (pos[0], pos[1]+int(line[1:]))
    if direction== 'W':
        pos = (pos[0], pos[1]-int(line[1:]))
    return pos

def move_to_r(face):
    if face == 'S':
        face = 'W'
        return face
    if face == 'W':
        face = 'N'
        return face
    if face == 'N':
        face = 'E'
        return face
    if face == 'E':
        face = 'S'
        return face

def move_to_l(face):
    if face == 'S':
        face = 'E'
        return face
    if face == 'E':
        face = 'N'
        return face
    if face == 'N':
        face = 'W'
        return face
    if face == 'W':
        face = 'S'
        return face

def move_to_waypoint(pos, waypoint, times):
    pos = (pos[0]+(waypoint[0]*times), pos[1]+(waypoint[1]*times))
    return pos

def rotate_waypoint_to_right(waypoint, line):
    times = (int(line[1:])//90)
    for i in range(0, times):
        if (waypoint[0] >= 0 and waypoint[1] >= 0):
            waypoint = (waypoint[1]*-1, waypoint[0])
        elif (waypoint[0] <= 0 and waypoint[1] >= 0):
            waypoint = (waypoint[1]*-1, waypoint[0])
        elif (waypoint[0] <= 0 and waypoint[1] <= 0):
            waypoint = (waypoint[1]*-1, waypoint[0])
        elif (waypoint[0] >= 0 and waypoint[1] <= 0):
            waypoint = (waypoint[1]*-1, waypoint[0])
    return waypoint

def rotate_waypoint_to_left(waypoint, line):
    times = (int(line[1:])//90)
    for i in range(0, times):
        if (waypoint[0] >= 0 and waypoint[1] >= 0):
            waypoint = (waypoint[1], waypoint[0]*-1)
        elif (waypoint[0] <= 0 and waypoint[1] >= 0):
            waypoint = (waypoint[1], waypoint[0]*-1)
        elif (waypoint[0] <= 0 and waypoint[1] <= 0):
            waypoint = (waypoint[1], waypoint[0]*-1)
        elif (waypoint[0] >= 0 and waypoint[1] <= 0):
            waypoint = (waypoint[1], waypoint[0]*-1)
    return waypoint

def get_input():
    f = open("input", "r")
    return [line for line in f.readlines()]

def solve(pos, waypoint, lines):

    for line in lines:
        if line[0] == 'F':
            pos = move_to_waypoint(pos, waypoint, int(line[1:]))
        if line[0] == 'N':
            waypoint = move('N', waypoint, line)
        if line[0] == 'S':
            waypoint = move('S', waypoint, line)
        if line[0] == 'E':
            waypoint = move('E', waypoint, line)
        if line[0] == 'W':
            waypoint = move('W', waypoint, line)
        if line[0] == 'R':
            waypoint = rotate_waypoint_to_right(waypoint, line)
        if line[0] == 'L':
            waypoint = rotate_waypoint_to_left(waypoint, line)

    result = abs(pos[0])+abs(pos[1])
    print(result)
    return result

def solve_part_one():
    f = open("input", "r")
    pos = (0,0)

    face = 'E';
    for line in f:
        if line[0] == 'F':
            pos = move(face, pos, line)
        if line[0] == 'N':
            pos = move('N', pos, line)
        if line[0] == 'S':
            pos = move('S', pos, line)
        if line[0] == 'E':
            pos = move('E', pos, line)
        if line[0] == 'W':
            pos = move('W', pos, line)

        if line[0] == 'R':
            for i in range(0,int(line[1:]) // 90):
                face = move_to_r(face)

        if line[0] == 'L':
            for i in range(0,int(line[1:]) // 90):
                face = move_to_l(face)


    result = abs(pos[0])+abs(pos[1])
    print(result)
    return result

if __name__ == '__main__':
    solve((0,0), (1,10), get_input())



