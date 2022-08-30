# 최소공배수
def gcd(a, b):
    x = max(a, b)
    y = min(a, b)
    while y:
        if x % y == 0:
            return y
        else:
            x, y = y, x % y

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    d = gcd(a, b)
    print(a * b // d)