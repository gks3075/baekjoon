import sys
p = sys.stdin.readline().strip()

stack = []
ppap = ["P", "P", "A", "P"]
answer = "NP"

for i in p:
    while len(stack) >= 4 and stack[-4:] == ppap:
        for _ in range(4):  # stack에서 PPAP 제거
            stack.pop()
        stack.append("P")   # 제거한 PPAP 대신 P 넣기
    stack.append(i)
    # print(stack)
if stack == ["P"] or stack == ppap:
    answer = "PPAP"

print(answer)