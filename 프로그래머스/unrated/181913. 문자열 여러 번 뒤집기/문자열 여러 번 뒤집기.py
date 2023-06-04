def solution(my_string, queries):
    answer = ''
    for query in queries:
        s, e = query[0], query[1]
        reverse = my_string[s:e+1]
        my_string = my_string[:s] + reverse[::-1] + my_string[e + 1:]
    answer = my_string
    return answer