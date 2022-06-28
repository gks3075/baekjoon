# N 과 M
def perm(i, N, s):
    if s == M:
        print(*select)
    else:
        for j in range(N):
            if used[j] == 0:
                select[i] = list[j]
                used[j] = 1
                perm(i + 1, N, s + 1)
                used[j] = 0


N, M = map(int, input().split())
list = [x for x in range(1, N + 1)]
used = [0] * (N + 1)
select = [0] * M
perm(0, N, 0)