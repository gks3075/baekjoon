T = int(input())
ans = 0
for t in range(T):
    num = [0] * 7
    dice = list(map(int, input().split()))
    for n in dice:
        num[n] += 1
    max_id = 0
    for i in range(1, 7):
        if num[i] >= num[max_id]:
            max_id = i
    if num[max_id] == 3:
        temp = 10000 + max_id * 1000
    elif num[max_id] == 2:
        temp = 1000 + max_id * 100
    else:
        temp = max_id * 100
    ans = max(ans, temp)
print(ans)