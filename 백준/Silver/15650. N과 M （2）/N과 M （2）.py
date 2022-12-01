# N과 M
def backtracking(i, pick):    # 현재 뽑은 수, 뽑은 수 리스트
    global N, M
    if i == N + 1:
        return
    if len(pick) == M:
        print(*pick)
        return
    for j in range(i, N):
        backtracking(j + 1, [*pick, numbers[j]])


N, M = map(int, input().split())
numbers = list(range(1, N + 1))
p = []
backtracking(0, p)
