# 다리 놓기
def comb(n, r):
    ans = 1
    if n == r:
        return ans
    for i in range(n, n - r, -1):
        ans *= i
    for j in range(1, r + 1):
        ans //= j
    return ans

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(comb(M, M - N))