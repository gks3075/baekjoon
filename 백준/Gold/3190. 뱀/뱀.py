# 뱀
from collections import deque

def dummy():
    dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    d = 0   # 이동방향
    t = 0   # 시간 (초)
    head = [0, 0]
    tail = [0, 0]
    visited = [[0] * N for _ in range(N)]
    visited[0][0] = 1
    snake = deque()     # 뱀의 좌표
    snake.append([0, 0])
    step = 0
    while True:
        t += 1
        hi, hj = head[0] + dir[d][0], head[1] + dir[d][1]
        if 0 <= hi < N and 0 <= hj < N and visited[hi][hj] == 0:
            head = [hi, hj]
            visited[hi][hj] = 1
            snake.append([hi, hj])
            if board[hi][hj] == 0:  #사과가 없을 때
                ti, tj = snake.popleft()
                visited[ti][tj] = 0
            else:       # 사과가 있을 때
                board[hi][hj] = 0
        else:
            return t
        if step < L:
            if t == change[step][0]:
                if change[step][1] == 'L':
                    d = (d - 1) % 4
                elif change[step][1] == 'D':
                    d = (d + 1) % 4
                step += 1


N = int(input())    # 보드의 크기
K = int(input())    # 사과 개수
board = [[0] * N for _ in range(N)]
for _ in range(K):
    a, b = map(int, input().split())
    board[a - 1][b - 1] = 1
L = int(input())    # 방향전환 횟수
change = [0] * L
for i in range(L):
    x, c = input().split()
    change[i] = [int(x), c]

ans = dummy()
print(ans)

