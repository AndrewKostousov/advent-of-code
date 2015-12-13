def parse(ch):
    if ch == '>':
        return [1, 0]
    elif ch == '<':
        return [-1, 0]
    elif ch == '^':
        return [0, 1]
    elif ch == 'v':
        return [0, -1]
    raise 'Invalid direction: ' + ch


def walk(directions, locations):
    current_location = (0, 0)
    locations.add(current_location)
    for d in directions:
        current_location = (current_location[0] + d[0], current_location[1] + d[1])
        locations.add(current_location)


chars = open('03.in').read()
all_locations = set()
all_dirs = map(parse, chars)
walk(all_dirs[0::2], all_locations)
walk(all_dirs[1::2], all_locations)
print len(all_locations)