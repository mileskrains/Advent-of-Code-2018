from collections import defaultdict


with open('input04-0.txt') as f:
    entries = [line for line in f]

entries.sort()
guardsleep = defaultdict(lambda: [0]*60)

for entry in entries:
    minute = int(entry[15:17])
    text = entry[19:].strip()
    if text[0] == "G":
        guard = text.split()[1]
    elif text[0] == 'f':
        sleepstart = minute
    elif text[0] == 'w':
        for m in range(sleepstart, minute):
            guardsleep[guard][m] +=1

sleeptots = [(sum(v), k) for k, v in guardsleep.items()]
sleeptots.sort()

gn = sleeptots[-1][1]
gs = guardsleep[gn]
print(gs.index(max(gs)) * int(gn[1:]))

sleepmax = [(max(v), k) for k, v in guardsleep.items()]
sleepmax.sort()

gn = sleepmax[-1][1]
gs = guardsleep[gn]
print(gs.index(max(gs)) * int(gn[1:]))
