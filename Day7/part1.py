from collections import deque

with open('input.txt') as reader:
  lines = [line.strip() for line in reader.readlines()]

grid = list()
for l in lines:
    grid.append(list(l))

rows = len(grid)
cols = len(grid[0])

# first find position of S 
res = 1
s_pos = [-1,-1]
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 'S':
            s_pos = [r,c]

beams = deque([s_pos])
seen = set(s_pos)

def add(r,c):
    if (r,c) in seen:
        return 
    seen.add((r,c))
    beams.append((r,c))

res = 0 

while len(beams) > 0:
    r,c = beams.popleft()
    if grid[r][c] == '.' or grid[r][c] == 'S':
        if r == len(grid) - 1: 
            continue 
        add(r+1, c)
    elif grid[r][c] == '^':
        res += 1
        add(r, c -1)
        add(r, c+1)

print(res)