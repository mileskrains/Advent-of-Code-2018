import string


with open('input05-0.txt') as f:
    input_polymer = f.read().strip()

polymer = [input_polymer, 'dabAcCaCBAcCcaDA'][1]

ords = [ord(c) for c in polymer]
print(len(ords))


def reacted_size(ords, dropchar='*'):
    pos2 = 1
    pos1 = 0

    drop_ords = (ord(dropchar.lower()), ord(dropchar.upper()))
    ords = [e for e in ords if e not in drop_ords]
    size = len(ords)

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


print(reacted_size(ords))

dropsizes = [(reacted_size(ords, letter), letter) for letter in string.ascii_lowercase]
print(sorted(dropsizes))
