import random

num_digits = 3
max_guess = 10


def main():
    print('Welcome to Bagels: A deductive logic game where you must guess a number based on clues!')

    while True: # main loop
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print('You have {} guesses to get it'.format(max_guess))

        num_guess = 1
        while num_guess <= max_guess: # input loop
            guess = ''
            while len(guess) != num_digits or not guess.isdecimal():
                print('Guess #{}: '.format(num_guess))
                guess = input('> ')

            #prints the clue

            clues = getClues(guess, secretNum)
            print(clues)
            num_guess += 1



            if guess == secretNum: #you win!
                break
            if num_guess > max_guess: #too many guesses
                print('You ran out of guesses')
                print('The answer was {}.'.format(secretNum))

        #want to play again?

        print('Do you want to play again? (yes or no)')
        if not input('>  ').lower().startswith('y'):
            break
    print(' Thanks for playing!')



def getSecretNum(): #defines the secretNum
    numbers = list('0123456789')
    random.shuffle(numbers)

    secretNum = ''

    for i in range(num_digits):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum): #calculates your clues
    if guess == secretNum:
        return 'You got it! Congratz!'
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)
    
if __name__ == '__main__':
    main()