def solution(num, total):
    answer = []
    if num % 2:
        m = total // num
        answer = [i for i in range(m - num // 2, m + num // 2 + 1)]
    else:
        m = total // num
        answer = [i for i in range(m - num // 2 + 1, m + num // 2 + 1)]
    return answer