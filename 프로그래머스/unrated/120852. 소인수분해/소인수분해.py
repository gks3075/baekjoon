def solution(n):
    answer = []
    sol = n
    for i in range(2, n + 1):
        if sol % i == 0:
            answer.append(i)
            while sol % i == 0:
                sol = sol // i
        
    return answer