# 치킨 쿠폰
while True:
    try:
        k, n = map(int, input().split())
        ans = k
        while k >= n:
            ans += k // n
            k = (k // n) + k % n
        print(ans)
    except:
        break