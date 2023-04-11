def solution(array, n):
    answer = 0
    min_n = 100
    array.sort()
    for x in array:
        if abs(n - x) < min_n:
            min_n = abs(n - x)
            answer = x
    return answer