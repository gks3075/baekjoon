# 단어 공부

word = input()

alpha = [0] * 26

for x in word:
    if ord(x) >= 97:
        i = ord(x) - 97
        alpha[i] += 1
    else:
        i = ord(x) - 65
        alpha[i] += 1

m = max(alpha)
cnt = 0
max_i = 0
for i in range(len(alpha)):
    if alpha[i] == m:
        max_i = i
        cnt += 1

if cnt == 1:
    print(chr(max_i + 65))
else:
    print('?')

