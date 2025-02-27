N, M = map(int, input().split())

n = [i for i in range(1, N + 1)]
for _ in range(M):
    i, j = map(int, input().split())
    n[i - 1], n[j - 1] = n[j - 1], n[i - 1]
print(*n)