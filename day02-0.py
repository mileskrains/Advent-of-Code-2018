from collections import Counter


ct_2 = 0
ct_3 = 0

with open('input02-0.txt') as f:
    for line in f:
        cts = Counter(line).values()
        if 2 in cts:
            ct_2 += 1
        if 3 in cts:
            ct_3 += 1

print(ct_2 * ct_3)