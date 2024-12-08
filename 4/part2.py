with open('input.txt', 'r') as file:
    data = file.read()

grid = data.splitlines()
rows, cols = len(grid), len(grid[0])

def getXMAS(r, c):
    posDiag = [(r + 1, c - 1), (r, c), (r - 1, c + 1)]
    negDiag = [(r - 1, c - 1), (r, c), (r + 1, c + 1)]

    directions = [posDiag, negDiag]

    def count(direction):
        word = ""
        for r, c in direction:
            if r not in range(rows) or c not in range(cols):
                return 0
            word += grid[r][c]
        if word == "MAS" or word == "SAM": return 1
        return 0

    res = 0
    for dir in directions:
        res += count(dir)

    return res

res = 0
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 'A':
            res += getXMAS(r, c) // 2 # only count if answer is 2 (which means both diagonals are correct)

print(res)
