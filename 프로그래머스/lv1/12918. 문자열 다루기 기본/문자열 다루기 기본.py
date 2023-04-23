def solution(s):
    answer = False
    if len(s) == 4 or len(s) == 6:
        flag = 1
        for x in s:
            if x >= '0' and x <= '9':
                pass
            else:
                flag = 0
                break
        if flag:
            answer = True
    return answer