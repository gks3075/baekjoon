def solution(numbers):
    answer = 0
    answer = sum(numbers) / len(numbers)
    answer = round(answer, 1)
    return answer