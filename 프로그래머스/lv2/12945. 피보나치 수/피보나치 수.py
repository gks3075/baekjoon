def solution(n):
    answer = 0
    a = 0
    b = 1
    for i in range(2, n + 1):
        answer = a + b
        a = b
        b = answer
    answer = answer % 1234567
    return answer