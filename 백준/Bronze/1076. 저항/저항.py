array = [['black', '0', '1'], ['brown', '1', '10'], ['red', '2', '100'], ['orange', '3', '1000'], ['yellow', '4', '10000'], ['green', '5', '100000'], ['blue', '6', '1000000'], ['violet', '7', '10000000'], ['grey', '8', '100000000'], ['white', '9', '1000000000']]

ans = ''
for i in range(3):
    x = input()
    if i == 2:
        for row in array:
            if x == row[0]:
                ans = int(ans)
                ans *= int(row[2])
    else:
        for row in array:
            if x == row[0]:
                ans += row[1]

print(ans)