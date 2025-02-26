s = list(input())

stack = [] # input으로 들어오는 문자열 길이를 추가하는 스택

for i in range(len(s)):
    if s[i] == ")":
        tmp = 0
        while True:
            t = stack.pop()
            if t == "(":
                n = stack.pop()
                stack.append(n * tmp)
                break
            else:
                tmp += t
    elif s[i] == "(":
        stack[-1] = int(s[i - 1])
        stack.append(s[i])
    else:
        stack.append(1)
    # print(stack)
print(sum(stack))