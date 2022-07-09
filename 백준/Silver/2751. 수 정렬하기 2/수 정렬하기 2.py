# 수 정렬하기 2
N = int(input())
list = [int(input()) for x in range(N)]
list.sort()
for i in range(N):
    print(list[i])