#로또
import sys
input = sys.stdin.readline

def perm(i, s, p):      # 뽑은 숫자 개수, 마지막 뽑은 수, 뽑은 수 리스트
    if i == 6:
        print(*p)
    for j in range(s, k):
        perm(i + 1, j + 1, p + [S[j]])

while True:
    tc = list(map(int, input().strip().split()))
    if tc[0] == 0:
        break
    k = tc[0]
    S = tc[1:]
    perm(0, 0, [])
    print()