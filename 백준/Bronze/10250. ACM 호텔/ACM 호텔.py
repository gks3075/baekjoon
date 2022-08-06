# ACM 호텔
T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    ans = 0
    if N % H == 0:
        ans += H * 100
        ans += N // H
    else:
        ans += (N % H) * 100
        ans += (N // H) + 1
    print(ans)