# 소수 찾기
N = int(input())
array = list(map(int, input().split()))

def prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

cnt = 0
for i in range(N):
    if prime(array[i]):
        cnt += 1

print(cnt)