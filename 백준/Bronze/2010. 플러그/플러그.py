# 플러그
N = int(input())
ans = 0
for i in range(N):
    ans += int(input())
print(ans - N + 1)