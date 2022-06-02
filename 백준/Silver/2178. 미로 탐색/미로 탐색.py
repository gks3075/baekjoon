# 미로 탐색
def bfs(i, j):
    global N, M
    q.append((i, j))
    visited[i][j] = 1
    while q:
        ci, cj = q.pop(0)
        if ci == N-1 and cj == M-1:
            return visited[ci][cj]
        for di, dj in d:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and maze[ni][nj] == 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[ci][cj] + 1



N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
q = []
min_cnt = N * M
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]

ans = bfs(0, 0)
print(ans)