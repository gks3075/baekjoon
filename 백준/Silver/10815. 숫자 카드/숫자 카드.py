# 숫자 카드
N = int(input())
num_N = list(map(int, input().split()))
M = int(input())
num_M = list(map(int, input().split()))

array = [0] * (20000001)
for i in range(N):
    array[num_N[i]] = 1

ans = [0] * M
for j in range(M):
    if array[num_M[j]] == 1:
        ans[j] = 1

print(*ans)