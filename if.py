number = 23
gunning = True
while gunning:
    guess = int(input('Enter an interger : '))
    if guess == number:
        #new block starts here
        print('Congratulations, you guessed it.')
        print('(but you do not win any prizes!)\n')
        #new block ends here
        gunning = False
    elif guess < number:
        #Another block
        print('No, it  is a little higher than that')
        #You can do what everyou want in a block....
    elif guess > number:
        print('No, it is a little lower than that')
        #you must have guessed > number to reach here
else:
    print('The while loop is over.')
print('Done')
#This last statement is always executed,
#after the if statement is executed.

