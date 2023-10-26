def solution(phone_number):
    answer = ''
    start = '*' * (len(phone_number) - 4)
    end = phone_number[-4:]
    answer = start + end
    return answer