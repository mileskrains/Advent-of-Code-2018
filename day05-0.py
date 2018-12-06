with open('input05-0.txt') as f:
    polymer = f.read().strip()

# polymer = 'dabAcCaCBAcaACZzcaDAZcDdCzaA'

ords = [ord(c) for c in polymer]
size = len(ords)
print(size)

use_version_2 = False

while True:
    if use_version_2:
        break
    for i in range(1, len(ords)):
        if abs(ords[i] - ords[i - 1]) == 32:
            ords[i] = 0
            ords[i - 1] = 0
    ords = [e for e in ords if e]
    if len(ords) == size:
        break
    else:
        size = len(ords)

# code below is more efficient, works for test input, but gives much higher answer for actual input

pos2 = 1
pos1 = 0

while use_version_2 and pos2 < size:
    # print(ords, pos1, pos2)
    if abs(ords[pos2]-ords[pos1]) == 32:
        ords[pos1] = 0
        ords[pos2] = 0
        pos2 += 1
        pos1 -= 1
        if pos1 < 0:
            pos1 += 1
    else:
        pos2 += 1
        pos1 = pos2 - 1

ords = [e for e in ords if e]
size = len(ords)
print(size)

# print(''.join([chr(o) for o in ords]))

