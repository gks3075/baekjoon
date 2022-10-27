# 이상한 곱셈
a, b = map(str, input().split())
ans = 0
for x in a:
    for y in b:
        ans += int(x) * int(y)
print(ans)