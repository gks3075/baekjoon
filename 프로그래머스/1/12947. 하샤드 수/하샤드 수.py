def solution(x):
    answer = True
    st = str(x)
    di = 0
    for i in st:
        di += int(i)
    if x % di != 0:
        answer = False
    return answer