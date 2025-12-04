def is_reachable(x,y,grid):
    # gets all adjacent 8 positions to the current x,y ()
    # return if toilet paper adjacent less than 4
    dirs = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (1,-1), (-1, 1)]
    rows = len(grid)
    cols = len(grid[0])
    res = 0
    for d in dirs:
        nx = x + d[0]
        ny = y + d[1]
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '@':
            # only check if in valid range
            res += 1 
    return res < 4




with open('input.txt') as reader:
  lines = [line.strip() for line in reader.readlines()]

grid = list()
for l in lines:
    grid.append(list(l))

rows = len(grid)
cols = len(grid[0])
res = 0
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == '@' and is_reachable(r,c,grid):
            res += 1

print(res)



