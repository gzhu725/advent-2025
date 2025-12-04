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
total_removed = 0

while True: 
    to_remove = list()

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@' and is_reachable(r, c, grid):
                to_remove.append((r, c))
    if not to_remove:
        break 
    
    for r, c in to_remove:
        grid[r][c] = '.'
    
    total_removed += len(to_remove)

print(total_removed)

