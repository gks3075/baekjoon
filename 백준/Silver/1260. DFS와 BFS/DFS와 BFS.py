# DFS BFS
from collections import deque
def dfs(V):
    dfs_visited[V] = 1
    print(V, end=' ')
    for i in range(len(array[V])):
        if array[V][i] and dfs_visited[i] == 0:
            dfs(i)

def bfs(V):
    q = deque()
    q.append(V)
    bfs_visited[V] = 1
    while q:
        c = q.popleft()
        print(c, end=' ')
        for i in range(len(array[c])):
            if array[c][i] and bfs_visited[i] == 0:
                bfs_visited[i] = 1
                q.append(i)


N, M, V = map(int, input().split())
array = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    array[a][b] = 1
    array[b][a] = 1

dfs_visited = [0] * (N + 1)
bfs_visited = [0] * (N + 1)

dfs(V)
print()
bfs(V)