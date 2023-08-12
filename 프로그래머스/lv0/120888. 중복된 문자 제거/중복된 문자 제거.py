def solution(my_string):
    answer = ''
    check = [0] * 500
    for x in my_string:
        if check[ord(x)] == 0:
            check[ord(x)] += 1
            answer += x
    
    return answer