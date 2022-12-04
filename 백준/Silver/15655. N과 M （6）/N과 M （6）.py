# N 과 M
def p(i, pick):
    if len(pick) == M:
        print(*pick)
        return
    if i == N:
        return
    for j in range(i, N):
        p(j + 1, pick + [numbers[j]])


N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
p(0, [])