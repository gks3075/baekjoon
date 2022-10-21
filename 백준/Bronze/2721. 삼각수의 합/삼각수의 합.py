T = int(input())

def cum(k):
    return k * (k + 1) // 2

for tc in range(T):
    n = int(input())
    ans = 0
    for i in range(1, n + 1):
        ans += i * cum(i + 1)
    print(ans)