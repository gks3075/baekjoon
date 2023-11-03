def solution(my_string):
    answer = 0
    for x in my_string:
        if '0' <= x <= '9':
            answer += int(x)
    return answer