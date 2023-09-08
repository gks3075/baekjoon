def solution(my_string, alp):
    answer = ''
    for x in my_string:
        if x == alp:
            answer += x.upper()
        else:
            answer += x
    return answer