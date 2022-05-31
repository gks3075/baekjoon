N = int(input())
con = int(input())
con_list = [[] for _ in range(N + 1)]

for i in range(con):
    a, b = map(int, input().split())
    con_list[a].append(b)
    con_list[b].append(a)

visited = [0] * (N + 1)

def dfs(i):
    visited[i] = 1
    for x in con_list[i]:
        if visited[x] == 0:
            dfs(x)


dfs(1)
print(sum(visited) - 1)