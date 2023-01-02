# 사탕 선생 고창영
T = int(input())
for _ in range(T):
    input()
    N = int(input())
    total = 0
    for n in range(N):
        total += int(input())
    if total % N == 0:
        print('YES')
    else:
        print('NO')