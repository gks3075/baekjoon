def solution(s):
    answer = []
    t = 0
    zero = 0
    
    while s != '1':
        tmp = 0
        for x in s:
            if x == '0':
                zero += 1
            else:
                tmp += 1

        t += 1
        # print(tmp)
        s = format(tmp, 'b')
        # print(s)
        # break
    return [t, zero]