import matplotlib.pyplot as plt


with open("input12-0.txt") as f:
    initial_state = f.readline().strip().split()[2]
    f.readline()
    rules = [line.strip().split() for line in f]

rule_dict = {r[0]: r[2] for r in rules}

pad_ct = 600
cg = '.'*pad_ct + initial_state + '.'*pad_ct


def report_score():
    potsum = 0
    for num, val in enumerate(cg):
        if val == '#':
            potsum += (num - pad_ct)
    return potsum

scores = []
for _ in range(500):
    ng = ['.', '.']
    for p in range(2, len(cg)-2):
        ng.append(rule_dict.get(cg[p-2:p+3],'.'))
    cg = ''.join(ng)+'..'
    scores.append(report_score())

plt.plot(scores)
plt.show()

steps = [t - s for s, t in zip(scores, scores[1:])]
print(steps[-25:])
print(scores[-1])

ans = scores[-1] + (50_000_000_000 - 500) * steps[-1]
print(ans)
