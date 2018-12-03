from collections import defaultdict


with open('input03-0.txt') as f:
    claims = [line.split()[2:] for line in f]

claimcounts = defaultdict(int)

for claim in claims:
    ox, oy = [o for o in claim[0][:-1].split(',')]
    ex, ey = [e for e in claim[1].split('x')]
    for x in range(int(ox), int(ox)+int(ex)):
        for y in range(int(oy), int(oy)+int(ey)):
            claimcounts[x, y] += 1

print(sum([1 for v in claimcounts.values() if v > 1]))

def proc_claim_line(line):
    parts = line.split()
    id = int(parts[0][1:])
    ox, oy = [int(p) for p in parts[2][:-1].split(',')]
    ex, ey = [int(p) for p in parts[3].split('x')]
    return (id, ox, oy, ex, ey)


with open('input03-0.txt') as f:
    claims = [proc_claim_line(line) for line in f]

claimants = defaultdict(list)

for claim in claims:
    id, ox, oy, ex, ey = claim
    for x in range(ox, ox+ex):
        for y in range(oy, oy+ey):
            claimants[x, y].append(id)

shared = set()

for entry in claimants.values():
    if len(entry) > 1:
        shared.update(entry)

all_ids = set(range(1, claims[-1][0]))
print(all_ids-shared)
