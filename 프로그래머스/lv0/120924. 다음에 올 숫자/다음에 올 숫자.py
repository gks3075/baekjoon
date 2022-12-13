def solution(common):
    answer = 0
    #등차수열여부확인
    if common[1] - common[0] == common[2] - common[1]:
        answer = common[-1] + common[1] - common[0]
    else:
        answer = common[-1] * (common[1] // common[0])
    return answer