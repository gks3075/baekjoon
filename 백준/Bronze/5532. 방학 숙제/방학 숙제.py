# 방학숙제
L = int(input())    # 방학일수
A = int(input())    # 국어
B = int(input())    # 수학
C = int(input())    # 국어
D = int(input())    # 수학

a = A // C
if A % C > 0:
    a += 1

b = B // D
if B % D > 0:
    b += 1

print(L - max(a, b))