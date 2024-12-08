with open('input.txt', 'r') as file:
    data = file.read()

equations = data.splitlines()

def concatenate(a, b):
    return int(str(a) + str(b))

def evaluate(equation):
    res, nums = equation.split(": ")
    nums = [int(n) for n in nums.split(" ")]

    def solve(i, total):
        if i == len(nums):
            return total if total == int(res) else 0

        return max(
            solve(i + 1, total + nums[i]),
            solve(i + 1, (total or 1) * nums[i]),
            solve(i + 1, concatenate((total or ""), nums[i]))
        )

    return solve(0, 0)

res = 0
for e in equations:
    res += evaluate(e)

print(res)
