# 가장 많은 글자
import sys
input = sys.stdin.read

s = input().replace("\n","").replace(" ","")
alpha = [0] * 26


for x in s:
    try:
        idx = ord(x) -97
        alpha[idx] += 1
    except:
        continue

max_l = max(alpha)
for i in range(26):
    if alpha[i] == max_l:
        print(chr(i + 97), end='')