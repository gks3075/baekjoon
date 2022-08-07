# 수 정렬하기
N = int(input())
array = [int(input()) for _ in range(N)]

array.sort()

for i in range(N):
    print(array[i])