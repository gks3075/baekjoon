def solution(numbers, k):
    answer = 0
    i = 0
    for n in range(k - 1):
        i = (i + 2) % len(numbers)
        print(i)
    answer = numbers[i]
    return answer