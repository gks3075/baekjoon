# 10부제
t = int(input())
n = list(map(int, input().split()))

ans = 0
for x in n:
    if x == t:
        ans += 1

print(ans)