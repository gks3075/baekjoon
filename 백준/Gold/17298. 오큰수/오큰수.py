import sys
N = int(sys.stdin.readline().strip())
l = list(map(int, sys.stdin.readline().split()))
answer = [-1] * N
stack = []

for i in range(N):
    while stack and l[stack[-1]] < l[i]:
        answer[stack.pop()] = l[i]
    stack.append(i)
    
print(*answer)