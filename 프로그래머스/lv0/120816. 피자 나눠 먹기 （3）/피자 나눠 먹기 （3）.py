def solution(slice, n):
    answer = 0
    for i in range(1, 51):
        if slice * i // n >= 1:
            answer = i
            break
    return answer