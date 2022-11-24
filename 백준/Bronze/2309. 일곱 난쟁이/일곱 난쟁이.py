height = [0] * 9
for i in range(9):
    h = int(input())
    height[i] = h

flag = 0
for i in range(9):
    for j in range(i + 1, 9):
        if sum(height) - height[i] - height[j] == 100:
            height.pop(i)
            height.pop(j - 1)
            flag = 1
            break
    if flag:
        break
height.sort()
for n in height:
    print(n)
