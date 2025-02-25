import sys
N = int(sys.stdin.readline().strip())
towers = list(map(int, sys.stdin.readline().split()))

answer = [0] * N
stack = [0]

for i in range(1, N):
    while stack and towers[stack[-1]] < towers[i]:
        stack.pop()
    if stack and towers[stack[-1]] >= towers[i]:
        answer[i] = stack[-1] + 1
    stack.append(i)
    
print(*answer)