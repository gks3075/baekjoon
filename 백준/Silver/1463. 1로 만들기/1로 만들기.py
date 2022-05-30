N = int(input())

dp = [0] * N
for i in range(1, N):
    if (N - i) * 3 <= N:
        dp[i] = min(dp[3*i-2*N], dp[2*i-N], dp[i-1]) + 1
    elif (N - i) * 2 <= N:
        dp[i] = min(dp[2*i-N], dp[i-1]) + 1
    else:
        dp[i] = dp[i-1] + 1
print(dp[-1])