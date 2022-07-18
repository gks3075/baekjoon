# 음식물 피하기
from collections import deque
def bfs(i, j):
    global cnt
    q = deque()
    q.append([i, j])
    visited[i][j] = 1
    while q:
        ci, cj = q.popleft()
        cnt += 1
        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            if 0 <= ni < N and 0 <= nj < M and array[ni][nj] == 1 and visited[ni][nj] == 0:
                q.append([ni, nj])
                visited[ni][nj] = 1




N, M, K = map(int, input().split())
array = [[0] * M for _ in range(N)]
for _ in range(K):
    a, b = map(int, input().split())
    array[a - 1][b - 1] = 1

visited = [[0] * M for _ in range(N)]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
ans = 0
cnt = 0

for i in range(N):
    for j in range(M):
        if array[i][j] == 1 and visited[i][j] == 0:
            cnt = 0
            bfs(i, j)
        if cnt > ans:
            ans = cnt

print(ans)

