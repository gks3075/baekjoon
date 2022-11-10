# 진짜 공간
N = int(input())
file = list(map(int, input().split()))
disk = int(input())

count = 0
for x in file:
    if x == 0:
        continue
    if x <= disk:
        count += 1
    else:
        count += (x // disk)
        if x % disk != 0:
            count += 1
print(disk * count)