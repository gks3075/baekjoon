def solution(strArr):
    answer = 0
    length = [0] * 31
    for x in strArr:
        length[len(x)] += 1
    for i in range(31):
        if length[i] > answer:
            answer = length[i]
    return answer