def solution(n, lost, reserve):
    answer = n
    lost.sort()
    reserve.sort()
    new_re = []
    for x in reserve:
        if x in lost:
            lost.remove(x)
        else:
            new_re.append(x)
    reserve = new_re
    for x in reserve:
        if x - 1 >= 1 and (x - 1) in lost:
            lost.remove(x - 1)
        elif x + 1 <= n and (x + 1) in lost:
            lost.remove(x + 1)
    answer = n - len(lost)
    return answer