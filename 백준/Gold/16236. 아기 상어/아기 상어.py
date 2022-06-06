# 아기상어
from collections import deque

def start():
    for i in range(N):
        for j in range(N):
            if array[i][j] == 9:
                return i, j

def find(i, j):
    global size
    q =  deque()
    q.append((i, j))
    visited = [[[0, 0] for _ in range(N)]  for _ in range(N)]
    visited[i][j] = [1, -1]
    while q:
        ci, cj = q.popleft()
        for di, dj in d:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and 0 < array[ni][nj] < size and visited[ni][nj][0] == 0:
                visited[ni][nj] = [visited[ci][cj][0] + 1, 1]
                q.append((ni, nj))
            elif 0 <= ni < N and 0 <= nj < N and (array[ni][nj] == size or array[ni][nj] == 0) and visited[ni][nj][0] == 0:
                visited[ni][nj] = [visited[ci][cj][0] + 1, 0]
                q.append((ni, nj))
    return visited

def min_start(v):
    for i in range(N):
        for j in range(N):
            if v[i][j][1] == 1:
                return 1, (i, j)
    return 0, (0, 0)

def eat(sti, stj, v):
    global t, eat_cnt, size, finish
    flag = 0
    minI, minJ = 0, 0
    flag, (minI, minJ) = min_start(v)
    for i in range(N):
        for j in range(N):
            if v[i][j][1] == 1 and v[minI][minJ][0] > v[i][j][0]:
                minI, minJ = i, j
    if flag:    # 먹을 물고기가 있으면
        array[sti][stj] = 0
        array[minI][minJ] = 9
        t += v[minI][minJ][0] - 1
        eat_cnt += 1
        if eat_cnt == size:
            size += 1   # 상어 크기 증가
            eat_cnt = 0     # 먹은 물고기 수 초기화
        return 1
    else:   # 먹을 물고기가 없으면
        return 0




N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]

t = 0
eat_cnt = 0
size = 2


d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
finish = 1

while finish:
    sti, stj = start()
    v = find(sti, stj)
    finish = eat(sti, stj, v)

print(t)



