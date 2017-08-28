import getpass
confession = None

print('Confession game, player one must guess who does player two likes.')

nameOne = input('What is your name? : ')
nameTwo = input('And, what is your name? : ')

name_confession = getpass.getpass(prompt='Who do you like?')

guess = input('Who do you think he/she likes? \n Your guess : ')

if guess.lower() == name_confession.lower():
    confession = True
    print('You guess it correctly')
else:
    print("Wrong guess")
    print('Player Two likes ', name_confession, ' not ', guess, '!')

if confession == True:
    print(nameOne, ' wins!')
else:
    print(nameTwo, ' wins!')
