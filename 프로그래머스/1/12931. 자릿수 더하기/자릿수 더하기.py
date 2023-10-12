def solution(n):
    answer = 0
    l = list(str(n))
    for x in l:
        answer += int(x)

    return answer