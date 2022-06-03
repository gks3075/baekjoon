# 유기농 배추
import sys
sys.setrecursionlimit(100000)

def dfs(i, j):
    visited[i][j] = 1
    for di, dj in d:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < M and array[ni][nj] == 1 and visited[ni][nj] == 0:
            dfs(ni, nj)


T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split())
    array = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        array[x][y] = 1

    visited = [[0] * M for _ in range(N)]
    d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    cnt = 0

    for i in range(N):
        for j in range(M):
            if array[i][j] == 1 and visited[i][j] == 0:
                cnt += 1
                dfs(i, j)
    print(cnt)