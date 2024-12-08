with open('input.txt', 'r') as file:
    data = file.read()

enabled = True

def toggleEnabled(i):
    pass

def parse(i):
    substr = data[i:]
    r = substr.index(")")
    if not enabled: return (0, r)
    if substr[0] != "(": return (0, r)
    nums = substr[1:r].split(",")
    if len(nums) != 2: return (0, r)
    for n in nums:
        if not n.isdigit(): return (0, r)
    return (int(nums[0]) * int(nums[1]), r)

res = 0

i = 0
while i < (len(data) - 2):
    if i + 4 <= len(data) and data[i:i+4] == "do()":
        enabled = True
    if i + 7 <= len(data) and data[i:i+7] == "don't()":
        enabled = False
    if data[i:i+3] == "mul":
        output, j = parse(i + 3)
        res += output
        i = max(i, j)
    i += 1

print(res)
