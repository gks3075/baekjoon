# 운동
N, m, M, T, R = map(int, input().split())
minute = 0
ans = 0
X = m
while minute < N:
    if m + T > M:
        ans = -1
        break
    if X + T <= M:
        minute += 1
        X += T
    else:
        X = max(m, X - R)
    ans += 1
print(ans)