paper = 0
ribbon = 0
lines = open('02.input').read().splitlines()
for line in lines:
    dimensions = [int(d) for d in line.split('x')]
    dimensions.sort()
    print dimensions
    paper += 3 * dimensions[0] * dimensions[1] + 2 * dimensions[0] * dimensions[2] + 2 * dimensions[1] * dimensions[2]
    ribbon += 2 * dimensions[0] + 2 * dimensions[1] + dimensions[0] * dimensions[1] * dimensions[2]
print(paper)
print(ribbon)