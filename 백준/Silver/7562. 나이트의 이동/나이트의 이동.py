# 나이트의 이동
from collections import deque

def bfs(start, I, finish):
    q = deque()
    q.append(start)
    visited = [[0] * I for _ in range(I)]
    visited[start[0]][start[1]] = 1
    d = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]
    while q:
        ci, cj = q.popleft()
        if ci == finish[0] and cj == finish[1]:
            return visited[ci][cj]
        else:
            for di, dj in d:
                ni, nj = ci + di, cj + dj
                if 0 <= ni < I and 0 <= nj < I and visited[ni][nj] == 0:
                    visited[ni][nj] = visited[ci][cj] + 1
                    q.append((ni, nj))

T = int(input())
for tc in range(1, T + 1):
    I = int(input())
    start = list(map(int, input().split()))
    finish = list(map(int, input().split()))

    ans = bfs(start, I, finish)
    print(ans - 1)