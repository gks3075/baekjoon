# 대칭 차집합
N, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = a + b
c = set(c)
L = len(c)
print(N + M -2 * (N + M - L))