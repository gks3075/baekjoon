# 그룹 단어 체커
def check(word):
    if len(word) == 1:
        return True
    alpa = [0] * 26
    alpa[ord(word[0]) - 97] += 1
    for i in range(1, len(word)):   # 알파벳이 연속이면
        if word[i - 1] == word[i]:
            alpa[ord(word[i]) - 97] += 1
        else:   # 알파벳이 연속이 아니면
            if alpa[ord(word[i]) - 97] == 0:
                alpa[ord(word[i]) - 97] += 1
            else:
                return False
    return True

N = int(input())
word_list = [0] * N
for i in range(N):
    word_list[i] = input()

cnt = 0
for i in range(N):
    if check(word_list[i]):
        cnt += 1

print(cnt)

