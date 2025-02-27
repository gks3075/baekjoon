import heapq
N = int(input())
n = [0] * N
for i in range(N):
    n[i] = int(input())

heapq.heapify(n)
answer = 0

while len(n) > 1:
    a = heapq.heappop(n)
    b = heapq.heappop(n)
    answer += a + b
    heapq.heappush(n, a + b)

print(answer)