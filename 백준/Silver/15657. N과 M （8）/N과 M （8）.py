# N 과 M
def p(i, l, pick):      # 고른 숫자 개수, 마지막으로 고른 숫자(비내림차순), 수열
    if len(pick) == M:
        print(*pick)
        return
    if i == N:
        return
    for j in range(l, N):
        p(i + 1, j, pick + [numbers[j]])

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

p(0, 0, [])