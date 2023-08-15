def solution(numbers, n):
    answer = 0
    for x in numbers:
        if answer <= n:
            answer += x
        else:
            break
    return answer