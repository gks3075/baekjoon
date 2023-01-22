# 피시방 알바
N = int(input())
h = list(map(int, input().split()))
check = [0] * 101
ans = 0
for i in h:
    if check[i] == 0:
        check[i] = 1
    else:
        ans += 1
print(ans)