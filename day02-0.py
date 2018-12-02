from collections import Counter


ct_2 = 0
ct_3 = 0

with open('input02-0.txt') as f:
    input_d2 = [line for line in f]

for line in input_d2:
    cts = Counter(line).values()
    if 2 in cts:
        ct_2 += 1
    if 3 in cts:
        ct_3 += 1

print(ct_2 * ct_3)


for i, w in enumerate(input_d2):
    for w2 in input_d2[i:]:
        if sum([a!=b for a,b in zip(w, w2)]) == 1:
            print(''.join([c for i, c in enumerate(w) if c==w2[i]]))



