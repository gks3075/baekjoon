T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    if a == 1:
        print(1)
    elif a % 10 == 0:
        print(10)
    else:
        ans = 1
        for i in range(b):
            ans = (ans * a) % 10
        print(ans)