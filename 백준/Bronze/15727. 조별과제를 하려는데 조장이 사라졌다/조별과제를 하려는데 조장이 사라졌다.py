L = int(input())

ans = L // 5
if L % 5 == 0:
    print(ans)
else:
    print(ans + 1)