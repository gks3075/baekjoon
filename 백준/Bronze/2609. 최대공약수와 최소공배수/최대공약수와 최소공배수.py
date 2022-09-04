# 최대공약수 최소공배수
def gcd(a,b):
    x = max(a, b)
    y = min(a, b)
    while True:
        if x % y == 0:
            return y
        else:
            x, y = y, x % y

a, b = map(int, input().split())
g = gcd(a, b)
print(g)
print(a * b // g)