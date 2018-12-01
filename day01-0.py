from itertools import cycle


with open('input01-0.txt') as f:
    freqlist = [int(line) for line in f]

print(sum(freqlist))

def find_repeated_freq(freqlist):
    freqcycle = cycle(freqlist)
    freq = 0
    freqs = {freq}

    for f in freqcycle:
        freq += f
        if freq in freqs:
            print(len(freqs) / len(freqlist))
            return freq
        else:
            freqs.add(freq)

assert find_repeated_freq([7, 7, -2, -7, -4]) == 14
print(find_repeated_freq(freqlist))