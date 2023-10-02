def solution(arr, intervals):
    answer = []
    for x in intervals:
        a, b = x[0], x[1]
        tmp = arr[a:b+1]
        answer = answer + tmp
    return answer