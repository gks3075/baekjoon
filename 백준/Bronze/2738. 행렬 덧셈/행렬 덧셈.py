# 행렬 덧셈
N, M = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]
b = [list(map(int, input().split())) for _ in range(N)]

ans = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        ans[i][j] = a[i][j] + b[i][j]

for k in range(N):
    print(*ans[k])