# 영역 구하기
from collections import deque

def rec(i1, j1, i2, j2):
    for i in range(i1, i2):
        for j in range(j1, j2):
            array[i][j] = 1

def bfs(i, j):
    d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    q= deque()
    q.append((i, j))
    visited[i][j] = 1
    a = 0
    while q:
        ci, cj = q.popleft()
        a += 1
        for di, dj in d:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and array[ni][nj] == 0 and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                q.append((ni, nj))
    return a


N, M, K = map(int, input().split())
array = [[0] * M for _ in range(N)]
for _ in range(K):
    a, b, c, d = map(int, input().split())
    rec(b, a, d, c)

cnt = 0
area = []
visited = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if array[i][j] == 0 and visited[i][j] == 0:
            cnt += 1
            area.append(bfs(i, j))

area.sort()
print(cnt)
print(*area)