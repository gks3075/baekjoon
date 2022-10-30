# 주사위
a, b, c = map(int, input().split())
num = [0] * 81
for i in range(1, a + 1):
    for j in range(1, b + 1):
        for k in range(1, c + 1):
            idx = i + j + k
            num[idx] += 1

max_idx = 0
for l in range(81):
    if num[max_idx] < num[l]:
        max_idx = l
print(max_idx)