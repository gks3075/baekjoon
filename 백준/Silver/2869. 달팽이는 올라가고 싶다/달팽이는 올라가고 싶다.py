# 달팽이
a, b, v = map(int, input().split())

target = v - a
gap = a - b
ans = target // gap + 1
if target % gap != 0:
    ans += 1

print(ans)