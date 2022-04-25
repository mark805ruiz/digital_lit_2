import random
import time


def displayIntro():
    print('You are in a land full of dragons. In front of you,')
    print('you see two caves. In one cave, the dragon is friendly')
    print('and will share his treasure with you. The other dragon')
    print('is greedy and hungry, and will eat you on sight.')
    print()

def chooseName():
    name = input('Choose a name\n')
    print('You have chosen %s as your name. We now begin...' % (name))
    return name
chooseName()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2' and cave!= '3':
        cave = input('Which cave will you go into? (1 or 2 or 3)\n')

    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 3)

    if chosenCave == 1:
         print('Gives you his treasure!')
    elif chosenCave == 2:
         print('Gobbles you down in one bite!')
    else: 
         print('fall to your death')
       

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':

    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    playAgain = input('Do you want to play again? (yes or no)')

