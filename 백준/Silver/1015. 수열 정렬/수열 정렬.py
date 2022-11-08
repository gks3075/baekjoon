# 수열 정렬
N = int(input())
array = list(map(int, input().split()))
tup = [0] * N

for i in range(N):
    tup[i] = [i, array[i]]

tup.sort(lambda x: x[1])

for i in range(N):
    tup[i] = [tup[i][0], i]
tup.sort(lambda x: x[0])

for x in tup:
    print(x[1], end=' ')