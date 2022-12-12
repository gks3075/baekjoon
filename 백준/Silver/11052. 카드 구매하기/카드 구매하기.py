#카드 구매하기
import sys
input = sys.stdin.readline

N = int(input())
price = list(map(int, input().split()))

dp = price.copy()
dp[1] = max(dp[1], dp[0] * 2)
for i in range(2, N):
    a = [dp[i - (j + 1)] + dp[j] for j in range(i // 2 + 1)]
    dp[i] = max([dp[i]] + a)

print(dp[N - 1])