import matplotlib.pyplot as plt
import numpy as np


def proc_line(line):
    xp = int(line[10:16])
    yp = int(line[18:24])
    xv = int(line[36:38])
    yv = int(line[40:42])
    return xp, yp, xv, yv


with open('input10-0.txt') as f:
    pt_dat = [proc_line(line) for line in f]

x, y, xv, yv = zip(*pt_dat)

xa = np.array(x)
ya = np.array(y)
xva = np.array(xv)
yva = np.array(yv)

steps = np.vstack((xa/xva, ya/yva))
steps = int(np.mean(np.abs(steps)))

xc = xa + (steps * xva)
yc = ya + (steps * yva)

plt.scatter(xc, yc)
plt.axes().set_aspect('equal')
plt.show()