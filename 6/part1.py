with open('input.txt', 'r') as file:
    data = file.read()

grid = [list(l) for l in data.splitlines()]
rows, cols = len(grid), len(grid[0])

def findStart():
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "^":
                return (r, c)
    return (0, 0)

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # up -> right -> down -> left
r, c = findStart()
d = 0

def nextDir(d):
    return d + 1 if d < 3 else 0

visit = set()

while r in range(rows) and c in range(cols):
    dr, dc = directions[d]
    visit.add((r, c))
    r, c = r + dr, c + dc
    if r in range(rows) and c in range(cols) and grid[r][c] == "#":
        r, c = r - dr, c - dc
        d = nextDir(d)

print(len(visit))
