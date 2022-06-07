# 안전 영역
from collections import deque
N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]

def find():
    minH = 101
    maxH = 0
    for i in range(N):
        for j in range(N):
            if minH > array[i][j]:
                minH = array[i][j]
            if maxH < array[i][j]:
                maxH = array[i][j]
    return minH, maxH

def flood(h):
    for i in range(N):
        for j in range(N):
            if array[i][j] > h:
                f[i][j] = 1

def bfs(i, j):
    d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in d:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and f[ni][nj]:
                visited[ni][nj] = 1
                q.append((ni, nj))


max_cnt = 1
minH, maxH = find()
for h in range(minH, maxH + 1):
    f = [[0] * N for _ in range(N)]
    flood(h)
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if f[i][j] and visited[i][j] == 0:
                cnt += 1
                bfs(i, j)

    if max_cnt < cnt:
        max_cnt = cnt

print(max_cnt)

