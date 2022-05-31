N = int(input())
array = [list(map(int, input())) for _ in range(N)]

def dfs(i, j):
    global cnt
    cnt += 1
    visited[i][j] = 1
    for di, dj in d:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and array[ni][nj] == 1:
            dfs(ni, nj)



cnt_list = []
visited = [[0] * N for _ in range(N)]
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]

for i in range(N):
    for j in range(N):
        if array[i][j] == 1 and visited[i][j] == 0:
            cnt = 0
            dfs(i, j)
            cnt_list.append(cnt)

cnt_list.sort()
print(len(cnt_list))
for n in cnt_list:
    print(n)