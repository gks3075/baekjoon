def solution(arr):
    answer = []
    s = -1
    e = -1
    for i in range(len(arr)):
        if arr[i] == 2:
            s = i
            break
    if s == -1:
        answer = [-1]
    else:
        for i in range(len(arr)):
            if arr[len(arr) - 1 - i] == 2:
                e = len(arr) - 1 - i
                break
        answer = arr[s: e + 1]
    return answer