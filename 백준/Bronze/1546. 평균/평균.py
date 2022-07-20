# 평균
N = int(input())
array = list(map(int, input().split()))

def mean(n):
    return sum(n) / len(n)

score = max(array)
for i in range(N):
    array[i] = array[i] / score * 100

ans = mean(array)

print(ans)