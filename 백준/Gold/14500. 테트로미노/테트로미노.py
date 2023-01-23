# 테트로미노
import sys
input = sys.stdin.readline

def dfs(si, sj, k, s):    # 시작 인덱스, 더한 횟수, 합
    global ans
    if k == 3:
        ans = max(ans, s)
        return
    for di, dj in d:
        ni, nj = si + di, sj + dj
        if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
            visited[ni][nj] = 1
            dfs(ni, nj, k + 1, s + tetro[ni][nj])
            visited[ni][nj] = 0

def check(si, sj, di, dj):
    ni, nj = si + di, sj + dj
    if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
        return True
    return False


N, M = map(int, input().strip().split())
tetro = [list(map(int, input().strip().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]

ans = 0
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, 0, tetro[i][j])
        visited[i][j] = 0
        tmp = 0
        if check(i, j, 0, 1) and check(i, j, 1, 0) and check(i, j, 0, -1):
            tmp += tetro[i][j] +  tetro[i][j + 1] + tetro[i + 1][j] + tetro[i][j - 1]
            ans = max(ans, tmp)
        tmp = 0
        if check(i, j, -1, 0) and check(i, j, 1, 0) and check(i, j, 0, -1):
            tmp += tetro[i][j] + tetro[i - 1][j] + tetro[i + 1][j] + tetro[i][j - 1]
            ans = max(ans, tmp)
        tmp = 0
        if check(i, j, -1, 0) and check(i, j, 0, 1) and check(i, j, 0, -1):
            tmp += tetro[i][j] + tetro[i - 1][j] + tetro[i][j + 1] + tetro[i][j - 1]
            ans = max(ans, tmp)
        tmp = 0
        if check(i, j, -1, 0) and check(i, j, 0, 1) and check(i, j, 1, 0):
            tmp += tetro[i][j] + tetro[i - 1][j] + tetro[i][j + 1] + tetro[i + 1][j]
            ans = max(ans, tmp)

print(ans)


