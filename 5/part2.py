from collections import defaultdict


with open('input.txt', 'r') as file:
    data = file.read()

rules, updates = [item.split("\n") for item in data.split("\n\n")]

orderMap = defaultdict(set)
for rule in rules:
    x, y = rule.split("|")
    orderMap[x].add(y)

def isUpdateValid(update):
    update = update.split(",")

    included = set()

    def checkPage(page):
        if len(orderMap[page]) == 0 or len(included) == 0: return True

        for nextPage in orderMap[page]:
            if nextPage in included: return False

        return True

    for page in update:
        if not checkPage(page):
            return False
        included.add(page)

    return True

# bubble sort
def sortUpdate(arr):
    for n in range(len(arr) - 1, 0, -1):
        swapped = False

        for i in range(n):
            cur, nxt = arr[i], arr[i + 1]
            if len(orderMap[nxt]) > 0 and cur in orderMap[nxt]:
               arr[i], arr[i + 1] = arr[i + 1], arr[i]
               swapped = True

        if not swapped:
            break

res = 0
for update in updates:
    if not update or isUpdateValid(update): continue
    update = update.split(",")
    sortUpdate(update)
    res += int(update[len(update) // 2])

print(res)
