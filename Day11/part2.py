from collections import defaultdict
from functools import cache
with open('input.txt') as reader:
    lines = [line.strip() for line in reader.readlines()]

d = dict()
for l in lines:
    key, value = l.split(':')
    value = value.split(' ')
    d[key] = value[1:]


@cache
def dfs(node, seen_dac, seen_fft):
    if node == "out":
        return 1 if seen_dac and seen_fft else 0
    
    total = 0
    
    for nxt in d.get(node, []):
        new_seen_dac = seen_dac or (nxt == "dac")
        new_seen_fft = seen_fft or (nxt == "fft")
        total += dfs(nxt, new_seen_dac, new_seen_fft)
    
    return total

# start from svr
ans = 0
for nxt in d["svr"]:
    ans += dfs(nxt, nxt == "dac", nxt == "fft")

print(ans)