fuel_grid = {}
grid_SN = 2866

for x in range(1, 301):
    for y in range(1, 301):
        rack_ID = x + 10
        fuel_grid[x, y] = int(str((rack_ID * y + grid_SN) * rack_ID)[-3]) - 5

max33 = -999

for x in range(1, 299):
    for y in range(1, 299):
        sum33 = 0
        for xc in [x, x+1, x+2]:
            for yc in [y, y+1, y+2]:
                sum33 += fuel_grid[xc, yc]
        if sum33 > max33:
            max33 = sum33
            botleft = x, y

print(botleft, max33)