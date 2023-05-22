def solution(number):
    answer = 0
    tmp = 0
    for x in number:
        tmp += int(x)
    answer = tmp % 9
    return answer