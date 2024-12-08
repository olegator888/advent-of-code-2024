from collections import defaultdict


with open('input.txt', 'r') as file:
    data = file.read()

rules, updates = [item.split("\n") for item in data.split("\n\n")]

orderMap = defaultdict(set)
for rule in rules:
    x, y = rule.split("|")
    orderMap[x].add(y)

def checkUpdate(update):
    if not update: return 0

    update = update.split(",")

    included = set()

    def checkPage(page):
        if len(orderMap[page]) == 0 or len(included) == 0: return True

        for nextPage in orderMap[page]:
            if nextPage in included: return False

        return True

    for page in update:
        if not checkPage(page):
            return 0
        included.add(page)

    return int(update[len(update) // 2])

res = 0
for update in updates:
   res += checkUpdate(update)

print(res)
