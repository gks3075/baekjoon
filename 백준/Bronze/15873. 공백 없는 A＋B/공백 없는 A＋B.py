num = input()
if len(num) == 2:
    a = int(num[0])
    b = int(num[1])
elif len(num) == 3:
    if num[1] == '0':
        a = int(num[0:2])
        b = int(num[2])
    elif num[2] == '0':
        a = int(num[0])
        b = int(num[1:3])
else:
    a = int(num[0:2])
    b = int(num[2:4])
print(a + b)