# 뉴턴과 사과
p = list(map(int, input().split()))
x, y, r = map(int, input().split())

ans = 0
for i in range(4):
    if p[i] == x:
        ans = i + 1
print(ans)