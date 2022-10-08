for _ in range(3):
    N = int(input())
    s = 0
    for i in range(N):
        n = int(input())
        s += n
    if s == 0:
        print(0)
    elif s > 0:
        print("+")
    else:
        print("-")