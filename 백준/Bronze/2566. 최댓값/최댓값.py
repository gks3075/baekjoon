# 최댓값
numbers = [list(map(int, input().split())) for _ in range(9)]

ans = 0
coordinate = [1] * 2
for i in range(9):
    for j in range(9):
        if ans < numbers[i][j]:
            ans = numbers[i][j]
            coordinate[0] = i + 1
            coordinate[1] = j + 1

print(ans)
print(*coordinate)

