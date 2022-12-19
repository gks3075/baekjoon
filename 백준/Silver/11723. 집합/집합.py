# 집합
import sys
input = sys.stdin.readline

M = int(input().strip())
S = [0] * 21

for _ in range(M):
    command = list(input().strip().split())

    if command[0] == 'add':
        S[int(command[1])] = 1
    elif command[0] == 'remove':
        S[int(command[1])] = 0
    elif command[0] == 'check':
        print(S[int(command[1])])
    elif command[0] == 'toggle':
        S[int(command[1])] = (S[int(command[1])] + 1) % 2
    elif command[0] == 'all':
        S = [1] * 21
    elif command[0] == 'empty':
        S = [0] * 21
