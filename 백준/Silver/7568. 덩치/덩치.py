# 덩치
N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]

rank = [0] * N
for i in range(N):
    x, y = array[i]
    t = 0
    for j in range(N):
        if array[j][0] > x and array[j][1] > y:
            t += 1
    rank[i] = t + 1

print(*rank)
