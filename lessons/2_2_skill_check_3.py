print('Let\'s find out if you are willing to to wait long enough to get the thing you want!')
print('Only type numbers for each of the following inputs.')
print('How much do you want to invest each month?')
invest = int(input())
print('How much do you need to have?')
need = int(input())
print('How long are you willing to wait?')
how_long = int(input())

month = 0

while invest * month < need:
    if month > how_long:
        print('You aren\'t willing to wait long enough. You need greater patince.')
        break
    month += 1
    if invest * month >= need:
        print('You will have to save for ' + str(month) + ' month/months.')
        break
    
