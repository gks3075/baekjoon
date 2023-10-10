def solution(n):
    answer = list(str(n))
    answer = answer[::-1]
    answer = [int(x) for x in answer]
    return answer