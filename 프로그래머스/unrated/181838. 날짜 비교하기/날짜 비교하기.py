def solution(date1, date2):
    answer = 0
    i = 0
    while i < 3:
        if date1[i] < date2[i]:
            answer = 1
            break
        elif date1[i] == date2[i]:
            i += 1
        else:
            break
        
            
    return answer