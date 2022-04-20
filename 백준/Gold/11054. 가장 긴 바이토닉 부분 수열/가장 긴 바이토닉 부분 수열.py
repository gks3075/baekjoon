# 가장 긴 바이토닉 부분 수열
N = int(input())
lst = list(map(int, input().split()))

dp1 = [1] * N
dp2 = [1] * N

for i in range(1, N):
    for j in range(i - 1, -1, -1):
        if lst[i] > lst[j]:
            dp1[i] = max(dp1[i], dp1[j] + 1)

for i in range(N - 1, -1, -1):
    for j in range(i + 1, N):
        if lst[i] > lst[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)

dp = [0] * N
for i in range(N):
    dp[i] = dp1[i] + dp2[i]
print(max(dp) - 1)
