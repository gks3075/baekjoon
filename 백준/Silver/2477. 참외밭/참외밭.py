# 참외밭
K = int(input())
length = [0] * 6
num = [0] * 5
for i in range(6):
    a, b = map(int, input().split())
    length[i] = [a, b]
    num[a] += 1

small = 1
big = 1
for i in range(6):
    if num[length[i][0]] == 1:
        big *= length[i][1]

for i in range(5, -1, -1):
    if length[i][0] == length[i - 2][0]:
        if length[i - 1][0] == length[i - 3][0]:
            small = length[i - 1][1] * length[i - 2][1]
            break

print(K * (big - small))
