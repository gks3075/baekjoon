# 약수 구하기
N, K = map(int, input().split())
ans = 0
cnt = 0
for i in range(1, N + 1):
    if N % i == 0:
        cnt += 1
    if cnt == K:
        ans = i
        break
print(ans)