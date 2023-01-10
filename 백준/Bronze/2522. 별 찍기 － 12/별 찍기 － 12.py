# 별 찍기 -12
N = int(input())
for i in range(N):
    print(' ' * (N - 1 - i) + '*' * (i + 1))
for i in range(1, N):
    print(' ' * i + '*' * (N - i))