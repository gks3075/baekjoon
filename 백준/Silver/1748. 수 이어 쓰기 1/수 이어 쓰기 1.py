# 수 이어 쓰기 1
N = int(input())

ans = 0
ten = 10
length = 1
for i in range(1, N + 1):
    if i < ten:
        ans += length
    else:
        ten *= 10
        length += 1
        ans += length
print(ans)
