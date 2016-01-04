result = 0
for line in open('08.in').read().splitlines():
    result += len(line) - len(eval(line))
print result
