def solution(n):
    answer = 1
    p = 1
    for i in range(1, n + 1):
        if p * i < n:
            p *= i
        elif p * i == n:
            answer = i
            break
        else:
            answer = i - 1
            break
    return answer