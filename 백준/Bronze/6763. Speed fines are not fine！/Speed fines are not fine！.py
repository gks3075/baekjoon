# Speed fines are not fine
limit = int(input())
speed = int(input())
over = speed - limit
if 1 <= over <= 20:
    print('You are speeding and your fine is $100.')
elif 21 <= over <= 30:
    print('You are speeding and your fine is $270.')
elif 31 <= over:
    print('You are speeding and your fine is $500.')
else:
    print('Congratulations, you are within the speed limit!')