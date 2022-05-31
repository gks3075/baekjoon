# 적록색약
import sys
sys.setrecursionlimit(100000)

N = int(input())
col_arr = [list(map(str, input())) for _ in range(N)]

def dfs1(i, j, c):
    visited1[i][j] = 1
    for di, dj in d:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < N and visited1[ni][nj] == 0 and col_arr[ni][nj] == c:
            dfs1(ni, nj, c)

def dfs2(i, j, c):
    visited2[i][j] = 1
    for di, dj in d:
        ni, nj = i + di, j + dj
        if c == 'R' or c == 'G':
            if 0 <= ni < N and 0 <= nj < N and visited2[ni][nj] == 0 and col_arr[ni][nj] in ['R', 'G']:
                dfs2(ni, nj, c)
        else:
            if 0 <= ni < N and 0 <= nj < N and visited2[ni][nj] == 0 and col_arr[ni][nj] == c:
                dfs2(ni, nj, c)


cnt1 = 0
cnt2 = 0
visited1 = [[0] * N for _ in range(N)]
visited2 = [[0] * N for _ in range(N)]
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]

for i in range(N):
    for j in range(N):
        if visited1[i][j] == 0:
            cnt1 += 1
            dfs1(i, j, col_arr[i][j])
        if visited2[i][j] == 0:
            cnt2 += 1
            dfs2(i, j, col_arr[i][j])

print(cnt1, cnt2)