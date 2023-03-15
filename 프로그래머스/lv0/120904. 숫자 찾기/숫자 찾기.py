def solution(num, k):
    answer = -1
    string = str(num)
    for i in range(len(string)):
        if str(k) == string[i]:
            answer = i + 1
            break
    return answer