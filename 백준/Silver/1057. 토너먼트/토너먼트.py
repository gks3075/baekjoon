# 토너먼트
N, a, b = map(int, input().split())
ans = 1
while True:
    a = (a + 1) // 2
    b = (b + 1) // 2
    if a == b:
        print(ans)
        break
    else:
        ans += 1