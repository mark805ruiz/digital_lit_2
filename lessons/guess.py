import random
name = input("What is your name? ")
number = random.randint(1, 100)
print('Hello ' + name + ', I\'m thinking of a number between 1 and 100')
guessesTaken = 0

while guessesTaken < 5:
    guess = input('Enter a guess: ')
    guess = int(guess)
    guessesTaken += 1
    if guess < number:
        print(str(guess) + ' is too low')
    elif guess > number:
        print(str(guess) + ' is too high')
    else:
        break
if guess == number:
    print('Winner!!!!! Congrats ' + name + ' you win')
else:
    print('You\'re a loser.')
