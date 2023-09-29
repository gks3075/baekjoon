def solution(food):
    answer = '0'
    s = ''
    e = ''
    for i in range(1, len(food)):
        n = food[i] // 2
        s = s + f'{i}' * n 
        e = f'{i}' * n + e
    answer = s + answer + e
    return answer