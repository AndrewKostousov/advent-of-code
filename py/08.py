result = 0
for line in open('08.in').read().splitlines():
    # result += len(line) - len(eval(line))
    result += 2 + line.count('\\') + line.count('\"')
print result
