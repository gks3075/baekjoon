# N 과 M
def com(i, pick):   # 뽑은 숫자 개수, 현재 숫자, 숫자 리스트
    global N, M
    if len(pick) == M:
        print(*pick)
        return
    if i == N:
        return


    for j in range(0, N):
        com(i + 1, [*pick, numbers[j]])


N, M = map(int, input().split())
numbers = [i for i in range(1, N + 1)]

p = []
com(0, p)