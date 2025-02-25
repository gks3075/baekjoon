import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

answer = [-1] * N
stack = [0]

# 각 숫자의 개수 count
F = [0] * (1000001)
for i in range(N):
    F[A[i]] += 1
    
# stack 에 입력해 놓고 조건이 맞는 원소는 추출하여 값을 입력한다.
for i in range(1, N):
    while stack and F[A[stack[-1]]] < F[A[i]]:
        answer[stack.pop()] = A[i]
    stack.append(i)

print(*answer)
    
