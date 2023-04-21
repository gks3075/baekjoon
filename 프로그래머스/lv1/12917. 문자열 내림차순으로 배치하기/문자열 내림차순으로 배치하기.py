def solution(s):
    answer = ''
    l = list(s)
    l.sort(reverse = True)
    answer = "".join(l)
    return answer