# 미국 스타일
T = int(input())
for _ in range(T):
    a, b = input().split()
    if b == 'kg':
        ans = float(a) * 2.2046
        print(f'{ans:.4f} lb')
    elif b == 'lb':
        ans = float(a) * 0.4536
        print(f'{ans:.4f} kg')
    elif b == 'l':
        ans = float(a) * 0.2642
        print(f'{ans:.4f} g')
    elif b == 'g':
        ans = float(a) * 3.7854
        print(f'{ans:.4f} l')