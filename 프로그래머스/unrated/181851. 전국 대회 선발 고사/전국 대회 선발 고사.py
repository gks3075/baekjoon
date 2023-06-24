def solution(rank, attendance):
    answer = 0
    new = []
    for i in range(len(attendance)):
        if attendance[i]:
            new.append([rank[i], i])
    new.sort()
    answer = 10000 * new[0][1] + 100 * new[1][1] + new[2][1]
    return answer