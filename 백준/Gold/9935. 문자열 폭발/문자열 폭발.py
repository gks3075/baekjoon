import sys
s = sys.stdin.readline().strip()
pattern = list(sys.stdin.readline().strip())

stack = []
for i in range(len(s)):
    stack.append(s[i])
    if s[i] == pattern[-1]:
        
        if stack[-len(pattern):] == pattern:
            for _ in range(len(pattern)):
                stack.pop()

if stack:
    print(''.join(stack))
else:
    print("FRULA")