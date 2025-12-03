with open('input.txt') as reader:
  lines = [line.strip() for line in reader.readlines()]

nums = lines 


def max_joltage(digits):
    stack = []
    to_remove = len(digits) - 12
    
    for digit in digits:
        # remove smaller digits from the stack if the current digit is bigger
        while stack and stack[-1] < digit and to_remove > 0:
            stack.pop()
            to_remove -= 1
        stack.append(digit)
    
    return int(''.join(stack[:12]))

res  = 0
for n in nums:
    res += (max_joltage(str(n)))

print(res)

