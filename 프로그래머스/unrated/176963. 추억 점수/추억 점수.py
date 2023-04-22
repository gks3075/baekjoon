def solution(name, yearning, photo):
    answer = []
    for p in photo:
        tmp = 0
        for n in p:
            for i in range(len(name)):
                if n == name[i]:
                    tmp += yearning[i]
                    break
        answer.append(tmp)
    return answer