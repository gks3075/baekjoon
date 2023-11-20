def solution(numbers):
    answer = []
    check = [0] * 200
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            check[numbers[i] + numbers[j]] = 1
    for i in range(len(check)):
        if check[i]:
            answer.append(i)
    return answer