from collections import defaultdict

with open('input07-0.txt') as f:
    step_order_pairs = [(line[5], line[36]) for line in f]

priors = defaultdict(list)
for bef, aft in step_order_pairs:
    priors[aft].append(bef)

priors_ext = {}
for aft, befs in priors.items():
    for bef in befs:
        if bef not in priors.keys():
            priors_ext[bef] = []
priors.update(priors_ext)

steps = []

while priors:
    avail = [k for k, v in priors.items() if not v]
    next_step = min(avail)
    steps.append(next_step)
    del priors[next_step]
    for aft, befs in priors.items():
        if next_step in befs:
            priors[aft].remove(next_step)

print(''.join(steps))