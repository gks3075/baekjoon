def solution(picture, k):
    answer = []
    for line in picture:
        tmp = ''
        for x in line:
            tmp += x * k
        answer += [tmp] * k
    return answer