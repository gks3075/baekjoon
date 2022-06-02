# 토마토
from collections import deque

def start():
    for i in range(N):
        for j in range(M):
            if array[i][j] == 1:
                q.append((i, j))
                visited[i][j] = 1
            elif array[i][j] == -1:
                visited[i][j] = -1

def bfs():
    start()
    while q:
        ci, cj = q.popleft()
        for di, dj in d:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and array[ni][nj] == 0 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[ci][cj] + 1

def ans():
    maxD = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0:
                return -1
            elif maxD < visited[i][j]:
                maxD = visited[i][j]
    return maxD - 1



M, N = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]

q = deque()
visited = [[0] * M for _ in range(N)]
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
bfs()

# print(visited)
print(ans())