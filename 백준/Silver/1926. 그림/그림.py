# 그림
from collections import deque

def bfs(i, j):
    cnt = 0
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    while q:
        ci, cj = q.popleft()
        cnt += 1
        for di, dj in d:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and array[ni][nj] == 1 and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                q.append((ni, nj))
    return cnt


N, M = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
cnt_list = []

for i in range(N):
    for j in range(M):
        if array[i][j] == 1 and visited[i][j] == 0:
            cnt_list.append(bfs(i, j))
if len(cnt_list) == 0:
    print(0)
    print(0)
else:
    print(len(cnt_list))
    print(max(cnt_list))