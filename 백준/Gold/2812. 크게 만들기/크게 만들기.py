import sys
N, K = map(int,sys.stdin.readline().split())
number = list(sys.stdin.readline().strip())

stack = []

for i in range(N):
    while K > 0 and stack and stack[-1] < number[i]:
        stack.pop()
        K -= 1
    stack.append(number[i])

if K > 0:
    print(''.join(stack[:-K]))
else:
    print(''.join(stack))
