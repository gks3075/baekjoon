# 가르침
import sys
input = sys.stdin.readline

def sol(i, s):  # 선택한 알파벳 수 , 마지막으로 선택한 알파벳
    global K, ans
    if i == K - 5:
        tmp = 0
        for word in words:
            flag = 1
            for x in word:
                if used[ord(x) - 97] == 0:
                    flag = 0
                    break
            if flag:
                tmp += 1
        ans = max(ans, tmp)
        return
    for j in range(s, 26):
        if used[j] == 0:
            used[j] = 1
            sol(i + 1, j + 1)
            used[j] = 0


N, K = map(int, input().split())
words = []
used = [0] * 26
given = ['a', 'c', 'i', 'n', 't']
for x in given:
    used[ord(x) - 97] = 1

ans = 0
if K < 5:
    print(ans)
elif 5 <= K <26:
    for i in range(N):
        check = [0] * 26
        word = input().strip()
        for x in word:
            check[ord(x) - 97] = 1
        if sum(check) <= K:
            words.append(word)
    sol(0, 0)

    print(ans)
else:
    print(N)