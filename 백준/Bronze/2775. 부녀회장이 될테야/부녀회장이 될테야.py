# 부녀회장이 될테야
array = [[0] * 15 for _ in range(15)]
for i in range(15):
    for j in range(1, 15):
        if i == 0:
            array[i][j] = j
        else:
            array[i][j] = array[i][j - 1] + array[i - 1][j]

T = int(input())
for _ in range(T):
    k = int(input()) # 층
    n = int(input()) # 호
    print(array[k][n])

