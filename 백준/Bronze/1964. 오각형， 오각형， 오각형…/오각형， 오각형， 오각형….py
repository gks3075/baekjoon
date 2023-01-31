# 오각형
N = int(input())

a = 5
d = 7
for i in range(N - 1):
    a += d
    d += 3

print(a % 45678)