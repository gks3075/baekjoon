# 세탁소 사장 동혁
T = int(input())
for tc in range(T):
    C = int(input())
    ans = [0] * 4
    mon = [25, 10, 5, 1]
    for i in range(4):
        ans[i] = C // mon[i]
        C = C % mon[i]
    print(*ans)