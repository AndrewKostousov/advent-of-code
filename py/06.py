import re

field = [[0 for x in range(1000)] for x in range(1000)]


def switch(instruction, x, y):
    if instruction == 'toggle':
        if field[x][y] == 0:
            field[x][y] = 1
            return 1
        else:
            field[x][y] = 0
            return -1
    elif instruction == 'on':
        result = int(field[x][y] == 0)
        field[x][y] = 1
        return result
    elif instruction == 'off':
        result = int(field[x][y] == 1) * -1
        field[x][y] = 0
        return result


def lit(instruction):
    delta = 0
    p1x = instruction[1][0]
    p1y = instruction[1][1]
    p2x = instruction[2][0]
    p2y = instruction[2][1]
    if p2x < p1x or p2y < p1y:
        raise 'p2 < p1'
    for x in range(p1x, p2x + 1):
        for y in range(p1y, p2y + 1):
            delta += switch(instruction[0], x, y)
    return delta


def parse(line):
    p = re.compile('\d+')
    coords = p.findall(line)
    p1 = (int(coords[0]), int(coords[1]))
    p2 = (int(coords[2]), int(coords[3]))
    if line.startswith('toggle'):
        return ('toggle', p1, p2)
    elif line.startswith('turn on'):
        return ('on', p1, p2)
    elif line.startswith('turn off'):
        return ('off', p1, p2)
    else:
        raise 'invalid input: ' + line


lights = 0
lines = open('06.in').read().splitlines()
for instruction in [parse(line) for line in lines]:
    lights += lit(instruction)
print lights
