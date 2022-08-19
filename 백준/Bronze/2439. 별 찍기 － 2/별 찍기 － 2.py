# 별 찍기 - 2
N = int(input())

ans = ' ' * N
for i in range(N):
    ans = ans[1:] + '*'
    print(ans)
