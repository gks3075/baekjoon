def solution(my_string):
    answer = 0
    tmp = ''
    flag = 0
    for x in my_string:
        if '0' <= x <= '9':
            tmp += x
            flag = 1
        else:
            if flag == 1:
                flag = 0
                answer += int(tmp)
                tmp = ''
    if flag:
        answer += int(tmp)
    return answer