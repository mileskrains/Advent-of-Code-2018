import string
from collections import Counter


with open('input05-0.txt') as f:
    input_polymer = f.read().strip()

polymer = [input_polymer, 'dabAcCaCBAcCcaDA'][0]
print(len(polymer))


def reacted_size(polymer):
    pos2 = 1
    pos1 = 0
    size = len(polymer)
    ords = [ord(c) for c in polymer]

    while pos2 < size:
        if abs(ords[pos2]-ords[pos1]) == 32:
            ords[pos1] = 0
            ords[pos2] = 0
            pos2 += 1
            pos1 -= 1
            if pos1 < 0:
                pos1 += 1
            elif ords[pos1] == 0:
                while ords[pos1] == 0:
                    pos1 -= 1
        else:
            pos2 += 1
            pos1 = pos2 - 1

    ords = [e for e in ords if e]
    return len(ords)


def reacted_size_ineff(polymer):
    ords = [ord(c) for c in polymer]
    size = len(ords)

    while True:
        for i in range(1, size):
            if abs(ords[i] - ords[i-1]) == 32:
                ords[i] = 0
                ords[i-1] = 0
        ords = [o for o in ords if o]
        rsize = len(ords)
        if rsize == size:
            break
        else:
            size = rsize

    return size



print(reacted_size(polymer))


def polydrop(polymer, dropchar):
    to_drop = (dropchar.lower(), dropchar.upper())
    return ''.join([ch for ch in polymer if ch not in to_drop])


dropsizes = [(reacted_size(polydrop(polymer, letter)), letter) for letter in string.ascii_lowercase]
print(sorted(dropsizes))

# print(sorted([(v, k) for k, v in Counter(polymer.lower()).items()], reverse=True))

# reacted_size above finds 'f' dropped gives reacted size of 6870, while reacted_size_ineff finds 'f' dropped gives reacted size of 6874 ...
