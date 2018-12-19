with open("input12-0.txt") as f:
    initial_state = f.readline().strip().split()[2]
    f.readline()
    rules = [line.strip().split() for line in f]

rule_dict = {r[0]: r[2] for r in rules}

pad_ct = 25
cg = '.'*pad_ct + initial_state + '.'*pad_ct

for _ in range(20):
    ng = ['.', '.']
    for p in range(2, len(cg)-2):
        ng.append(rule_dict.get(cg[p-2:p+3],'.'))
    cg = ''.join(ng)+'..'

potsum = 0
for num, val in enumerate(cg):
    if val == '#':
        potsum += (num - pad_ct)
print(potsum)