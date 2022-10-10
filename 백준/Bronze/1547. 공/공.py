M = int(input())
array = [0, 1, 0, 0]
for _ in range(M):
    x, y = map(int, input().split())
    array[x], array[y] = array[y], array[x]
    # print(array)
for i in range(4):
    if array[i]:
        print(i)