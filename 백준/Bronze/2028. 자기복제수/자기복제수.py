# 자기복제수
T = int(input())

for _ in range(T):
    n = input()
    square = int(n) * int(n)
    l = len(n)
    s = str(square)
    s = s[-l:]
    if s == n:
        print("YES")
    else:
        print("NO")