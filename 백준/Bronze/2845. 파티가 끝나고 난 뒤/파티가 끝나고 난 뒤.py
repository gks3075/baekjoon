# 파티가 끝나고 난 뒤
L, P = map(int, input().split())
article = list(map(int, input().split()))
ans = [0] * 5

p = L * P
for i in range(5):
    ans[i] = article[i] - p
print(*ans)