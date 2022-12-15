# 부분수열의 합
import sys
input = sys.stdin.readline

def perm(i, s):     # 현재 뽑은 숫자 개수, 합
    global ans
    if i > 0 and s == S:
        ans += 1
    if i == N:
        return
    for j in range(i, N):
        if used[j] == 0:
            used[j] = 1
            perm(j + 1, s + numbers[j])
            used[j] = 0

N, S = map(int, input().split())
numbers = list(map(int, input().strip().split()))

ans = 0
used = [0] * N
perm(0, 0)
print(ans)