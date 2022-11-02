# 성택이의 은밀한 비밀번호
T = int(input())
for _ in range(T):
    N = input()
    if 6 <= len(N) <= 9:
        print('yes')
    else:
        print('no')