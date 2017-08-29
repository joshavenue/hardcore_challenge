import random

def play_game():
    try:
        x = int(input('Enter your lower number : '))
        y = int(input('Enter your upper number : '))
        limit = int(input('How many times a player can guess? : '))
    except ValueError:
        print('Error within inputs.')
    else:
        pass

        random_number = random.randint(x,y)
        guess_time = []

        while len(guess_time) < limit:
            try:
                guess = int(input('Enter your guess : '))
            except ValueError:
                print('{} is not a number'.format(guess))
            else:

                if guess == random_number:
                    print('CORRECT! The number is indeed {}!'.format(random_number))
                    break
                else:
                    print('Try again!')

                guess_time.append(guess)

        else:
            print('GG. It was {}'.format(random_number))

        try_again = input('Do you wish to try again? Y/N : ')

        if try_again.lower() == 'y':
            play_game()
        elif try_again.lower() == 'n':
            print('GG.')
        else:
            print('Not sure that was a yes or not.')

play_game()
