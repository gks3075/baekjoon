# 숨바꼭질
def bfs(i):
    global K
    q = []
    q.append(i)
    visited[i] = 1
    while q:
        ci = q.pop(0)
        if ci == K:
            return visited[ci]
        else:
            for ni in [ci - 1, ci + 1, 2 * ci]:
                if 0 <= ni <= 100000 and visited[ni] == 0:
                    visited[ni] = visited[ci] + 1
                    q.append(ni)



N, K = map(int, input().split())
visited = [0] * 100001

ans = bfs(N)
print(ans - 1)
