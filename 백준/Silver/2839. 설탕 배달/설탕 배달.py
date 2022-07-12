# 설탕배달
N = int(input())

ans = -1
for i in range((N // 3) + 1):
    n = N - (3 * i)
    if n % 5 == 0:
        ans = n // 5 + i
        break
print(ans)