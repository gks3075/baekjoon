# 트리 순회
def pre_order(v):
    if v != '.':
        print(arr[v][0], end='')
        pre_order(arr[v][1])
        pre_order(arr[v][2])

def in_order(v):
    if v != '.':
        in_order(arr[v][1])
        print(arr[v][0], end='')
        in_order(arr[v][2])

def post_order(v):
    if v != '.':
        post_order(arr[v][1])
        post_order(arr[v][2])
        print(arr[v][0], end='')

N = int(input())
arr = {}
for i in range(N):
    a, b, c = input().split()
    arr[a] = [a,b, c]
pre_order('A')
print()
in_order('A')
print()
post_order('A')
print()