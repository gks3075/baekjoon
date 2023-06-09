def solution(myStr):
    answer = []
    sep = ['a', 'b', 'c']
    tmp = ''
    for i in range(len(myStr)):
        if myStr[i] in sep:
            if len(tmp) != 0:
                answer.append(tmp)
            tmp = ''
        else:
            tmp += myStr[i]
    if len(tmp) != 0:
        answer.append(tmp)
    if len(answer) == 0:
        answer = ['EMPTY']
    return answer