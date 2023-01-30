#트로피 진열
N = int(input())
tropy = [0] * N
left = 0
right = 0
check = 0
for i in range(N):
    tropy[i] = int(input())
    if tropy[i] > check:
        left += 1
        check = tropy[i]

check = 0
for j in range(N - 1, -1, -1):
    if tropy[j] > check:
        right += 1
        check = tropy[j]
print(left)
print(right)