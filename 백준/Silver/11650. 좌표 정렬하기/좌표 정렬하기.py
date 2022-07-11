#좌표 정렬하기
N = int(input())
list = [0] * N
for i in range(N):
    x, y = map(int, input().split())
    list[i] = [x, y]

list.sort(key=lambda x : (x[0], x[1]))
for i in range(N):
    print(*list[i])

