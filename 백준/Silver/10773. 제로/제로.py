# 제로
N = int(input())
array = [0] * N
top = 0
for i in range(N):
    a = int(input())
    if a == 0:
        top -= 1
        array[top] = 0
    else:
        array[top] = a
        top += 1

print(sum(array))