# 짝수를 찾아라
T = int(input())
for _ in range(T):
    m = 100
    total = 0
    numbers = list(map(int, input().split()))
    for x in numbers:
        if x % 2 == 0:
            m = min(m, x)
            total += x
    print(total, m)