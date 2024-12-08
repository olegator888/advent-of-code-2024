with open('input.txt', 'r') as file:
    data = file.read()

reports = [[int(n) for n in l.split(" ")] for l in data.splitlines()]

def checkReport(report):
    type = None # 1 - increasing, -1 - decreasing
    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]
        abs_diff = abs(diff)
        if type == None:
            type = 1 if diff > 0 else -1
        if (
            diff == 0
            or abs_diff < 1
            or abs_diff > 3
            or type == -1 and diff > 0
            or type == 1 and diff < 0
        ): return False
    return True

res = 0

for r in reports:
    for i in range(len(r)):
        if checkReport(r[:i] + r[i + 1:]):
            res += 1
            break

print(res)
