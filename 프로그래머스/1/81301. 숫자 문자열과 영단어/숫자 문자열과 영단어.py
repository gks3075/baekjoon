def solution(s):
    answer = 0
    number = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(10):
        s = s.replace(number[i], str(i))
    answer = int(s)
    return answer