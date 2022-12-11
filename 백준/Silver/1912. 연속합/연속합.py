# 연속합
import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

dp = array.copy()
for i in range(1, n):
    dp[i] = max(dp[i - 1] + dp[i], dp[i])

print(max(dp))