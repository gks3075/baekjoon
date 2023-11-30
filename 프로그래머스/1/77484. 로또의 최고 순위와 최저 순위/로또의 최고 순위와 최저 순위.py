def solution(lottos, win_nums):
    answer = [0] * 2
    check = 0
    no = 0
    for n in lottos:
        if n:
            if n in win_nums:
                check += 1
        else:
            no += 1
    answer[1] = min(7 - check, 6)
    answer[0] = min(7 - check - no, 6)
    return answer