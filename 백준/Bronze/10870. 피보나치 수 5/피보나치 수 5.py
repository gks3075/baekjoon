# 피보나치 수 5
def pibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return pibo(n-1) + pibo(n-2)

N = int(input())
ans = pibo(N)
print(ans)