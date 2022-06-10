# 수 찾기
def binary(x):
    global N
    start = 0
    finish = N -1
    while start <= finish:
        mid = (start + finish) // 2
        if x == A[mid]:
            print(1)
            return
        elif x < A[mid]:
            finish = mid - 1
        elif x > A[mid]:
            start = mid + 1
    print(0)
    return



N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
B = list(map(int, input().split()))

for m in B:
    binary(m)