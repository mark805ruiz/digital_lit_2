def playAgain():
    while True:
        yesOrNo = input("Do you want to play again? Type yes or no.\n")
        if yesOrNo == 'yes' or yesOrNo == 'Yes':
            return True
        if yesOrNo == 'no' or yesOrNo == 'No':
            return False
 
keepPlaying = True
while keepPlaying:
    keepPlaying = playAgain()
