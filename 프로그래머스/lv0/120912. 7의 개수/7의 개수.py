def solution(array):
    answer = 0
    for x in array:
        for letter in str(x):
            if letter == '7':
                answer += 1
    return answer