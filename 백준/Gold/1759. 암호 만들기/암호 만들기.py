# 암호 만들기
def password(i, p, v, c, s): # 글자 갯수, 비밀번호, 모음 포함 유무(0, 1), 자음 갯수, 알파벳 순으로 for문을 돌리기 위한 변수
    global L, C
    if i == L:
        if v and c >= 2:
            print(p)
        return
    for a in range(s, C):
        if alphabets[a] in vowels:
            password(i + 1, p + alphabets[a], 1, c, a + 1)
        else:
            if v == 0:
                password(i + 1, p + alphabets[a], 0, c + 1, a + 1)
            else:
                password(i + 1, p + alphabets[a], 1, c + 1, a + 1)


L, C = map(int, input().split())
alphabets = list(map(str, input().split()))
alphabets.sort()
vowels = ['a', 'e', 'i', 'o', 'u']

password(0, '', 0, 0, 0)


