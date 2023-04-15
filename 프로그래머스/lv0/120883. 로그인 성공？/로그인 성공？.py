def solution(id_pw, db):
    answer = 'fail'
    for x in db:
        if id_pw[0] == x[0]:
            if id_pw[1] == x[1]:
                answer = 'login'
            else:
                answer = 'wrong pw'
    return answer