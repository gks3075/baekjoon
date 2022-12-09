# 외판원 순회 2
import sys
input = sys.stdin.readline

def perm(i, p):      # 선택한 숫자의 개수, 선택한 숫자의 배열, 비용의 합
    global ans
    if i == N:
        total = 0
        for k in range(N - 1):
            total += cost[p[k]][p[k + 1]]
        if cost[p[N - 1]][p[0]] != 0:
            total += cost[p[N - 1]][p[0]]
            ans = min(ans, total)
        return
    for j in range(N):
        if used[j] == 0 and (i == 0 or cost[p[i - 1]][j]):
            used[j] = 1
            perm(i + 1, p + [j])
            used[j] = 0


N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]
used = [0] * N
ans = 1000000 * N * N

perm(0, [])
print(ans)