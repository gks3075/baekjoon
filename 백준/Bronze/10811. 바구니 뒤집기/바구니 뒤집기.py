N, M = map(int, input().split())

n = [i for i in range(1, N + 1)]

for _ in range(M):
    i, j = map(int, input().split())
    tmp = n[i -1 : j]
    tmp.reverse()
    n[i - 1 : j] = tmp
print(*n)