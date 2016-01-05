from sets import Set

import sys


def route_dist(route):
    dist = 0
    for i in range(0, len(route) - 1):
        dist += graph[(route[i], route[i + 1])]
    return dist


def all_perms(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]


graph = {}
vertices = Set()
for line in open('09.in').read().splitlines():
    parts = line.split(' = ')
    edge = parts[0].split(' to ')
    dist = int(parts[1])
    graph[(edge[0], edge[1])] = dist
    graph[(edge[1], edge[0])] = dist
    vertices.add(edge[0])
    vertices.add(edge[1])
print vertices
min_route = []
max_route = []
min_route_dist = sys.maxint
max_route_dist = 0
for route in all_perms(list(vertices)):
    dist = route_dist(route)
    if dist < min_route_dist:
        min_route_dist = dist
        min_route = route
    if dist > max_route_dist:
        max_route_dist = dist
        max_route = route
print min_route_dist, min_route
print max_route_dist, max_route
