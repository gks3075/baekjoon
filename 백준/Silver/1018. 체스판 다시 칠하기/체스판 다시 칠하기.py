#체스판
def check(i, j):
    cnt1 = 0
    cnt2 = 0
    for x in range(8):
        for y in range(8):
            if (x + y) % 2 == 0:
                if array[i + x][j + y] == "W":
                    cnt1 += 1
                else:
                    cnt2 += 1
            else:
                if array[i + x][j + y] == "B":
                    cnt1 += 1
                else:
                    cnt2 += 1
    return min(cnt1, cnt2)


M, N = map(int, input().split())
array = [list(map(str, input())) for _ in range(M)]

result = [65] * (M) * (N)
for i in range(0, M - 7):
    for j in range(0, N - 7):
        result[i*N + j] = check(i, j)

print(min(result))