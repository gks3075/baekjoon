# 좌료 정렬하기 2
N = int(input())
array = [0] * N
for i in range(N):
    a, b = map(int, input().split())
    array[i] = [a, b]

array.sort(key= lambda x: [x[1], x[0]])
for i in range(N):
    print(*array[i])