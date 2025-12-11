with open('input.txt') as reader:
  lines = [line.strip() for line in reader.readlines()]

grid = list()
for l in lines:
    grid.append(list(map(int, l.split(','))))

def area(c1, c2):
    # take two coords 
    return (abs(c1[0] - c2[0]) + 1) * (abs(c1[1] - c2[1]) + 1)

res = -1
for i in range(len(grid)):
    for j in range(i + 1, len(grid)):
        res = max(res, area(grid[i], grid[j]))

print(res)
