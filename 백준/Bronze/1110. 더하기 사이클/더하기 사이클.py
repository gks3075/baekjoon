# 더하기 사이클
N = int(input())
ans = 0
num = N
while True:
    if num < 10:
        num = num * 11
    else:
        f = (num // 10) + (num % 10)
        num = (num % 10) * 10 + f % 10
    ans += 1
    if num == N:
        break
print(ans)