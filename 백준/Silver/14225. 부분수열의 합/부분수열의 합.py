# 부분수열의 합
def perm(i, t):     # 뽑은 숫자, 합
    if i == N:
        check[t] = 1
        return
    perm(i + 1, t + S[i])
    perm(i + 1, t)

N = int(input())
S = list(map(int, input().split()))

check = [0] * (100000 * 20)
perm(0, 0)

for i in range(1, len(check)):
    if check[i] == 0:
        print(i)
        break

