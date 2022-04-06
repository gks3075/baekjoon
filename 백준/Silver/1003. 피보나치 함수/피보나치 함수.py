# 피보나치 함수
def fibonachi(N):
    if N == 0:
        arr[N][0] = 1
        return
    elif N == 1:
        arr[N][1] = 1
        return
    else:
        arr[N][0] = arr[N - 1][0] + arr[N - 2][0]
        arr[N][1] = arr[N - 1][1] + arr[N - 2][1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    arr = [[0] * 2 for _ in range(N + 1)]
    for i in range(N + 1):
        fibonachi(i)
    print(f'{arr[N][0]} {arr[N][1]}')
