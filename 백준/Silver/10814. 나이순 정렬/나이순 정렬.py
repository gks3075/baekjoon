# 나이순 정렬
N = int(input())
member = [0] * N
for i in range(N):
    a, b = map(str, input().split())
    member[i] = [int(a), b]

member.sort(key= lambda x: x[0])
for i in range(N):
    print(*member[i])