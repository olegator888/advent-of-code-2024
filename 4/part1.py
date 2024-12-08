with open('input.txt', 'r') as file:
    data = file.read()

grid = data.splitlines()
rows, cols = len(grid), len(grid[0])

def getXMAS(r, c):
    right = [(r, c + i + 1) for i in range(3)]
    left = [(r, c - i - 1) for i in range(3)]
    down = [(r + i + 1, c) for i in range(3)]
    up = [(r - i - 1, c) for i in range(3)]
    upright = [(r - i - 1, c + i + 1) for i in range(3)]
    upleft = [(r - i - 1, c - i - 1) for i in range(3)]
    downright = [(r + i + 1, c + i + 1) for i in range(3)]
    downleft = [(r + i + 1, c - i - 1) for i in range(3)]

    directions = [right, left, down, up, upright, upleft, downright, downleft]

    def count(direction):
        word = "X"
        for r, c in direction:
            if r not in range(rows) or c not in range(cols):
                return 0
            word += grid[r][c]
        return 1 if word == "XMAS" else 0

    res = 0
    for dir in directions:
        res += count(dir)

    return res

res = 0
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 'X':
            res += getXMAS(r, c)

print(res)
