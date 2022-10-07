S = input()
alpha = [0] * 26

for x in S:
    alpha[ord(x) - 97] += 1
print(*alpha)