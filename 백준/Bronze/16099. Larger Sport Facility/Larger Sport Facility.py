# Larger Sport Facility
T = int(input())
for _ in range(T):
    a, b, c, d = map(int, input().split())
    if a * b < c * d:
        print('Eurecom')
    elif a * b == c * d:
        print('Tie')
    else:
        print('TelecomParisTech')