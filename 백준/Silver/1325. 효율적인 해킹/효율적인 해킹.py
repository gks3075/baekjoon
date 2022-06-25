from collections import deque

def bfs(i):
    global cnt
    q = deque()
    q.append(i)
    visited[i] = 1
    while q:
        ci = q.popleft()
        cnt += 1
        for j in link[ci]:
            if visited[j] == 0:
                visited[j] = 1
                q.append(j)


N, M = map(int, input().split())
link = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    link[b].append(a)
cnt_list = [0] * (N + 1)
for i in range(1, N + 1):
    cnt = 0
    visited = [0] * (N + 1)
    bfs(i)
    cnt_list[i] = cnt

max_cnt = max(cnt_list)
max_list = []
for i in range(N + 1):
    if cnt_list[i] == max_cnt:
        max_list.append(i)

print(*max_list)