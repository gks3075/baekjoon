# 구간 합 구하기 4
N, M = map(int, input().split())
array = list(map(int, input().split()))
cum = [0] * (N + 1)
for i in range(N):
    cum[i + 1] = cum[i] + array[i]

for _ in range(M):
    i, j = map(int, input().split())
    print(cum[j] - cum[i - 1])
