# solution taken from Jonathan Paulson (shapely, polygon?!)
import shapely 

with open('input.txt') as reader:
  lines = [line.strip() for line in reader.readlines()]

grid = list()
for l in lines:
    grid.append(list(map(int, l.split(','))))

polygon = shapely.Polygon(grid)
shapely.prepare(polygon)

def area(c1, c2):
    # take two coords 
    return (abs(c1[0] - c2[0]) + 1) * (abs(c1[1] - c2[1]) + 1)

res = 0 
for i in grid:
    for j in grid:
        corners = [i, (i[0], j[1]), j, (j[0], i[1])]
        a = area(i, j)
        rect = shapely.Polygon(corners)
        if polygon.contains(rect) and a > res:
            res = a

print(res)