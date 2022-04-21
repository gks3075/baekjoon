l1 = input()
l2 = input()

lcs = [[0] * (len(l1) + 1) for _ in range(len(l2) + 1)]

for i in range(len(l2)):
    for j in range(len(l1)):
        if l2[i] == l1[j]:
            lcs[i + 1][j + 1] = lcs[i][j] + 1
        else:
            lcs[i + 1][j + 1] = max(lcs[i][j + 1], lcs[i + 1][j])

print(lcs[-1][-1])