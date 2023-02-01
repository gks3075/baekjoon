# 영식이와 친구들
N, M, L = map(int, input().split())
check = [0] * N
count = 0
i = 0
check[i] = 1
while max(check) < M:
    if check[i] % 2 == 0:
        i = (i - L) % N
    else:
        i = (i + L) % N
    check[i] += 1
    count += 1
print(count)