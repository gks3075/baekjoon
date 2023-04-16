def solution(score):
    answer = []
    rank = []
    for s in score:
        rank.append(sum(s))
    rank.sort(reverse=True)
    for s in score:
        for i in range(len(rank)):
            if sum(s) == rank[i]:
                answer.append(i + 1)
                break
    return answer