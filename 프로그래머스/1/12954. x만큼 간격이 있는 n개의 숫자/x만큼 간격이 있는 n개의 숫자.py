def solution(x, n):
    answer = []
    st = 0
    for i in range(n):
        st += x
        answer.append(st)
    return answer