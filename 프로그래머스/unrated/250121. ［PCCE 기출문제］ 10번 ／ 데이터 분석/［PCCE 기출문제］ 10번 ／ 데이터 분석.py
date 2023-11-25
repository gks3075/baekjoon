def solution(data, ext, val_ext, sort_by):
    answer = []
    terms = ['code', 'date', 'maximum', 'remain']
    pick = 0
    s = 0
    for i in range(4):
        if ext == terms[i]:
            pick = i   
        if sort_by == terms[i]:
            s = i
    for d in data:
        if d[pick] < val_ext:
            answer.append(d)
    answer.sort(key = lambda x: x[s])
    return answer