# FBI
flag = 1
for i in range(1, 6):
    name = input()
    if 'FBI' in name:
        flag = 0
        print(i, end=' ')
if flag:
    print('HE GOT AWAY!')