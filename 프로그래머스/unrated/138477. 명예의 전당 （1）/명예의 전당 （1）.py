def solution(k, score):
    answer = []
    hall = []
    for x in score:
        if len(hall) < k:
            hall.append(x)
        else:
            if x > hall[0]:
                hall[0] = x
        hall.sort()
        answer.append(hall[0])
    return answer