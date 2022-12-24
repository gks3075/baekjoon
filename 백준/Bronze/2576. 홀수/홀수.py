# 홀수
total = 0
minN = 100
flag = 1

for _ in range(7):
    n = int(input())
    if n % 2 == 1:
        flag = 0
        total += n
        minN = min(minN, n)

if flag:
    print(-1)
else:
    print(total)
    print(minN)