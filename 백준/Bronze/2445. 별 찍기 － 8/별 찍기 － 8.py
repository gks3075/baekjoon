# 별 찍기 - 8
N = int(input())
for i in range(1, N + 1):
    print(f'{"*" * (i)}{" " * (2*(N - i))}{"*" * (i)}')
for i in range(1, N):
    print(f'{"*" * (N - i)}{" " * (2*i)}{"*" * (N - i)}')