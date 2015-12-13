import hashlib

prefix = 'ckczppom'
suffix = 0
while True:
    suffix += 1
    m = hashlib.md5()
    m.update(prefix + str(suffix))
    if m.hexdigest().startswith('000000'):
        break
print suffix