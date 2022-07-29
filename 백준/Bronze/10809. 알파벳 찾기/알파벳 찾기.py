# 알파벳 찾기
s = input()
alpha = [-1] * 26

for i in range(len(s)):
    n = ord(s[i]) - 97
    if alpha[n] == -1:
        alpha[n] = i
print(*alpha)

