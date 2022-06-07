# 섬의 개수
from collections import deque
def bfs(i, j):
    d = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in d:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < h and 0 <= nj < w and visited[ni][nj] == 0 and array[ni][nj]:
                visited[ni][nj] = 1
                q.append((ni, nj))


while 1:
    w, h = map(int, input().split())    # 너비 높이
    if w == 0 and h == 0:
        break
    array = [list(map(int, input().split())) for _ in range(h)]

    visited = [[0] * w for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if array[i][j] and visited[i][j] == 0:
                cnt += 1
                bfs(i, j)

    print(cnt)
