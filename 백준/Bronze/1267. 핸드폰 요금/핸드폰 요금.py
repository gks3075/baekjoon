N = int(input())
array = list(map(int, input().split()))

def yunsik(a):
    return (a // 30 + 1) * 10

def minsik(a):
    return (a // 60 + 1) * 15

y = 0
m = 0
for x in array:
    y += yunsik(x)
    m += minsik(x)

if y < m:
    print(f"Y {y}")
elif m < y:
    print(f'M {m}')
else:
    print(f'Y M {y}')