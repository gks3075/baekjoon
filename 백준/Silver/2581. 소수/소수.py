# 소수
M = int(input())
N = int(input())

def prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num = []
for i in range(M, N + 1):
    if prime(i):
        num.append(i)

if len(num) == 0:
    print(-1)
else:
    print(sum(num))
    print(num[0])
