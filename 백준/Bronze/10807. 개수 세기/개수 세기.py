N = int(input())
array = list(map(int, input().split()))
v = int(input())

cnt = 0
for x in array:
    if x == v:
        cnt += 1
print(cnt)