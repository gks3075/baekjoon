# 농구경기
N = int(input())
initial = [0] * 26
for _ in range(N):
    name = input()
    i = ord(name[0]) - 97
    initial[i] += 1

ans = ''
for i in range(26):
    if initial[i] >= 5:
        ans += chr(i + 97)

if len(ans) > 0:
    print(ans)
else:
    print("PREDAJA")