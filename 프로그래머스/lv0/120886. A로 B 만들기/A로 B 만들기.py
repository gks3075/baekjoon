def solution(before, after):
    answer = 0
    b = list(before)
    a = list(after)
    b.sort()
    a.sort()
    ans_b = "".join(b)
    ans_a = "".join(a)
    if ans_b == ans_a:
        answer = 1
    return answer