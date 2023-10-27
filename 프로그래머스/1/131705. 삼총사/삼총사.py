def solution(number):
    answer = 0
    check = 0
    for i in range(len(number) - 2):
        check += number[i]

        for j in range(i + 1, len(number) - 1):
            check += number[j]

            for k in range(j + 1, len(number)):
                check += number[k]

                if check == 0:
                    answer += 1
                check -= number[k]
            check -= number[j]
        check -= number[i]
                
    return answer