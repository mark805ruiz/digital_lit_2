print('What do you want to buy?', end = ' ')
food = input()
print('How much do(es) the ' + food + ' cost?', end = ' ')
cost = int(input())
print('How much money do you have to buy ' + food + '?', end = ' ')
money = int(input())
if money >= cost:
    print('You can afford it!')
else:
    print('You can\'t afford it. Don\'t buy it!')
