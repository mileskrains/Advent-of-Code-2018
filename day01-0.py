
freq = 0

with open('input01-0.txt') as f:
    for line in f:
        freq += int(line)

print(freq)

