name_First = input('What is your name? \n First name : ')
name_Last = input('Last name : ')

list(name_First)
list(name_Last)

display_initial = 'You have an initial of {}'.format(''.join(name_First[0]))
display_last = 'You have a last initial name of {}'.format(''.join(name_Last[0]))

print(display_initial)
print(display_last)
