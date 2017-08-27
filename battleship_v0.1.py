print ('Your enemy\'s ship is hiding between Coordinate 1 , 1 till 10.\nYou need to plot your attack')

print('Player One')
x = input('Coordinate X : ')
y = input('Coordinate Y : ')

print('Player Two')
a = input('Coordinate X : ')
b = input('Coordinate Y : ')

number_x = [ int(x) for x in x ]
number_y = [ int(y) for y in y ]
number_a = [ int(a) for a in a ]
number_b = [ int(b) for b in b ]

attack_coordinate = [number_x,number_y]
enemy_coordinate = [number_a,number_b]

if not attack_coordinate == enemy_coordinate:
    print('Hit wrong location')
    print('Enemy is hiding in coordination :', enemy_coordinate)
    print('You lose')
elif len(x) == 0 and len(y) == 0:
    print('You didn\'t even try!')
elif len(a) == 0 and len(b) == 0:
    print('Enemy is out of the map.')
else:
    print('Bullseye.')
    print('Player One wins')
