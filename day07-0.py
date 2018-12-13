from collections import defaultdict

with open('input07-0.txt') as f:
    step_order_pairs = [(line[5], line[36]) for line in f]


def gen_priors():
    priors = defaultdict(list)
    for bef, aft in step_order_pairs:
        priors[aft].append(bef)

    priors_ext = {}
    for aft, befs in priors.items():
        for bef in befs:
            if bef not in priors.keys():
                priors_ext[bef] = []
    priors.update(priors_ext)

    return priors


priors = gen_priors()
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


def task_time(ltr):
    return ord(ltr) - 4


priors = gen_priors()
time = -1
worker_ct = 5
active = []

while priors or active:
    time += 1
    # clear finished tasks from active list
    for task, finish in active:
        if time == finish:
            active.remove((task, finish))
            for aft, befs in priors.items():
                if task in befs:
                    priors[aft].remove(task)

    # replenish active list from available tasks and workers
    avail = sorted([k for k, v in priors.items() if not v])
    while avail and len(active) < worker_ct:
        next_active = avail.pop(0)
        active.append((next_active, time + task_time(next_active)))
        del priors[next_active]

print()
print(time)
