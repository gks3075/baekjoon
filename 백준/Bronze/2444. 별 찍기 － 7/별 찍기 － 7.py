N = int(input())
for i in range(1, N):
    print(f'{" " * (N - i)}{"*" * (2*i - 1)}')
for i in range(N):
    print(f'{" " * (i)}{"*" * (2*(N - i) - 1)}')