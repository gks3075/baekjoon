# 지능형 기차
ans = 0
maxN = 0
for _ in range(4):
    o, i = map(int, input().split())
    ans = ans - o + i
    if ans > maxN:
        maxN = ans

print(maxN)