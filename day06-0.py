from collections import defaultdict


with open('input06-0.txt') as f:
    coords = [tuple(int(part.strip()) for part in line.split(','))
              for line in f]

xs, ys = zip(*coords)
cc = len(xs)

coords = list(zip(xs, ys, range(1, len(xs)+1)))

xmin, xmax = min(xs), max(xs)
ymin, ymax = min(ys), max(ys)

def nearest_id(xc, yc):
    dists = [(abs(xc-x)+abs(yc-y), id) for (x, y, id) in coords]
    nd, ni = min(dists)
    dc = [d for d, i in dists if d == nd]
    if len(dc) > 1:
        return 0
    else:
        return ni

id_nc = defaultdict(int)
edge_ids = set()

for x in range(xmin, xmax+1):
    for y in range(ymin, ymax+1):
        nid = nearest_id(x, y)
        id_nc[nid]+=1
        if (x == xmin or x == xmax or
            y == ymin or y == ymax):
            edge_ids.add(nid)

interior_regions = [(v, k) for k, v in id_nc.items() if k not in edge_ids]
interior_regions.sort(reverse=True)
print(interior_regions[0])