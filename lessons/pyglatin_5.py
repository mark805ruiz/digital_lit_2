print ('Welcome to the Pig Latin Translator!')

original = input('What\'s your name\n')

print('You entered: ' + original)

length = len(original)
length = int(length)

if length > 0 and original.isalpha():
  print('Your length is ' + str(length) + ', which is greater than 0')
else:
  print('empty, since we have a non character letter')
