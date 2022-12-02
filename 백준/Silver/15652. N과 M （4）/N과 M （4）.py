# N 과 M
def comb(i, s, pick):
    if len(pick) == M:
        print(*pick)
        return
    if i == N:
        return
    for j in range(s, N):
        comb(i + 1, j, [*pick, numbers[j]])


N, M = map(int, input().split())
numbers = [i for i in range(1, N + 1)]
p = []
comb(0, 0, p)