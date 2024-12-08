from collections import defaultdict


with open('input.txt', 'r') as file:
    data = file.read()

lines = data.splitlines()

left, right = [], []
for line in lines:
    l, r = [int(num) for num in line.split()]
    left.append(l)
    right.append(r)
rightCnt = defaultdict(int)
for n in right:
    rightCnt[n] += 1
res = sum([l * rightCnt[l] for l in left])
print(res)
