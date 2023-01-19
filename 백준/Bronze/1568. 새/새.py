# 새
N = int(input())

ans = 0
i = 1
while N > 0:
    if N - i >= 0:
        ans += 1
        N -= i
        i += 1
    else:
        i = 1
print(ans)