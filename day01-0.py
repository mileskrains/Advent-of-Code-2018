from itertools import cycle


freqlist = []

with open('input01-0.txt') as f:
    for line in f:
        freqlist.append(int(line))

print(sum(freqlist))

freqcycle = cycle(freqlist)
freq = 0
freqs = {freq}

for f in freqcycle:
    freq += f
    if freq in freqs:
        print(freq)
        break
    else:
        freqs.add(f)