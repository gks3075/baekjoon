def solution(n):
    answer = 2
    for i in range(2, n):
        if n == i * i:
            answer = 1
            break
    return answer