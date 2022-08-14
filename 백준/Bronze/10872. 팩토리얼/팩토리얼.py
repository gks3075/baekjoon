# 팩토리얼
N = int(input())

def pac(N):
    if N == 0:
        return 1
    if N == 1:
        return 1
    return N * pac(N - 1)
print(pac(N))