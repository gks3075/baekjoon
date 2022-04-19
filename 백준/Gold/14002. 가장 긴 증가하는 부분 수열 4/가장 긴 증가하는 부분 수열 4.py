# 가장 긴 증가하는 부분 수열 4
N = int(input())
lst = list(map(int, input().split()))
dp = [1] * N

for i in range(1, N):
    for j in range(i-1, -1, -1):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i], dp[j] + 1)

max_id = 0
for i in range(N):
    if dp[max_id] < dp[i]:
        max_id = i
print(dp[max_id])

lis = [0] * dp[max_id]
tmp = max_id
lis[dp[tmp] - 1] = lst[tmp]
for j in range(max_id - 1, -1, -1):
    if dp[j] == dp[tmp] - 1:
        tmp = j
        lis[dp[tmp] - 1] = lst[tmp]

print(*lis)