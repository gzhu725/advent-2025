from collections import deque
from functools import cache 

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

@cache
def solve(r,c):
    if r >= len(grid):
        return 1
    
    if grid[r][c] == '.' or grid[r][c] == 'S':
        return solve(r + 1, c)
    elif grid[r][c] == '^':
        return solve(r, c - 1) + solve(r, c + 1)

print(solve(s_pos[0], s_pos[1]))