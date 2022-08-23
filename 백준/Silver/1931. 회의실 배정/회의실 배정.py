# 회의실 배정
N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]

array.sort(key=lambda x: (x[1], x[0]))

ans = 1
last = array[0]
for i in range(1, N):
    if array[i][0] >= last[1]:
        ans += 1
        last = array[i]
print(ans)

