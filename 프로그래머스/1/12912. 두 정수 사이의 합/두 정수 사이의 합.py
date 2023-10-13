def solution(a, b):
    answer = 0
    if a == b:
        answer = a
    else:
        answer = (a + b) * (abs(a - b) + 1) // 2
    return answer