def solution(order):
    answer = 0
    for x in order:
        if "americano" in x:
            answer += 4500
        elif "cafelatte" in x:
            answer += 5000
        elif "anything" in x:
            answer += 4500
    return answer