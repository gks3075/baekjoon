def solution(n):
    answer = '수박' * (n // 2 + n % 2)
    answer = answer[:n]
    return answer