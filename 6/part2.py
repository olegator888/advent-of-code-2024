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

def findLoop():
    r, c = findStart()
    d = 0

    def nextDir(d):
        return d + 1 if d < 3 else 0

    visit = set()

    loopFound = False

    while True:
        dr, dc = directions[d]

        if (r, c, d) in visit:
            loopFound = True
            break

        visit.add((r, c, d))
        r, c = r + dr, c + dc

        if r not in range(rows) or c not in range(cols):
            break

        if grid[r][c] == "#":
            r, c = r - dr, c - dc
            d = nextDir(d)

    return loopFound

res = 0
for r in range(rows):
    for c in range(cols):
        if grid[r][c] != ".":
            continue
        grid[r][c] = "#"
        if findLoop(): res += 1
        grid[r][c] = "."

print(res)
