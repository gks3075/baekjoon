def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        numbers[i] = 2 * numbers[i]
    
    return numbers