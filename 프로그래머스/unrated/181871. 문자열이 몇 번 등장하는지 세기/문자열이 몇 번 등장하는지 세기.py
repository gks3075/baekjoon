def solution(myString, pat):
    answer = 0
    for i in range(len(myString) - len(pat) + 1):
        if myString[i] == pat[0]:
            flag = 1
            for j in range(1, len(pat)):
                if myString[i + j] != pat[j]:
                    flag = 0
                    break
            if flag:
                answer += 1
            
    return answer