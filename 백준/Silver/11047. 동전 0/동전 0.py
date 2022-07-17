# 동전
N, K = map(int, input().split())
array = list(int(input()) for _ in range(N))

price = 0
cnt = 0

for i in range(N - 1, -1, -1):
    x = array[i]
    while price <= K:
        cnt += 1
        price += x
    price -= x
    cnt -= 1
    if price == K:
        break


print(cnt)

