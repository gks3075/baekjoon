# N 과 M
def p(i, pick):
    if len(pick) == M:
        print(*pick)
        return
    if i == N:
        return
    for j in range(N):
        if used[j] == 0:
            used[j] = 1
            p(i + 1, pick + [numbers[j]])
            used[j] = 0

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
used = [0] * N

p(0, [])
