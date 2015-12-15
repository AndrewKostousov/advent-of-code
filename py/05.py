def is_nice_1(s):
    for forbidden in ['ab', 'cd', 'pq', 'xy']:
        if forbidden in s:
            return False
    vowels = s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u')
    if vowels < 3:
        return False
    for i in range(0, len(s) - 1):
        if s[i] == s[i + 1]:
            return True
    return False


def is_nice_2(s):
    is_nice = False
    for i in range(0, len(s) - 2):
        if s[i] == s[i + 2]:
            is_nice = True
            break
    if not is_nice:
        return False
    is_nice = False
    for i in range(0, len(s) - 3):
        for j in range(i + 2, len(s) - 1):
            if s[i] == s[j] and s[i + 1] == s[j + 1]:
                is_nice = True
                break
    return is_nice


nice = 0
lines = open('05.in').read().splitlines()
for line in lines:
    nice += is_nice_2(line)
print nice
