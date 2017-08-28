print ('You are planning to set a working hour for your first employee')

x1 = input(str('Should he work from monday to friday? : '))
x2 = input(str('Is weekend off? :'))

y1 = input('What time should he comes to work? (In A.M) \n Time In :')
y2 = input('What time should he leaves work? (In P.M) \n Time Out : ')

start_work = ['7','8','9','10','11']
leave_time = ['5','6','7']

if 'y' in x1:
    print('He should work from Monday to Friday')
elif 'n' in x1:
    print('He will never work from Monday to Friday')
else:
    print('I do not understand your replies')

if 'n' in x2:
    print('Weekend is off!')
elif 'y' in x2:
    print('Man, you are rough.')
else:
    print('Not sure what you meant.')

if y1 in start_work:
    print('Good time to start.')
elif y1 == '':
    print('What timing actually?')
elif y1 not in start_work:
    print('Pretty sure it\'s too early')
else:
    print('Try again')

if y2 in leave_time:
    print('Standard leave time!')
elif y2 == '':
    print('What time again?')
elif y2 not in leave_time:
    print('Strange time to leave.')
else:
    print('Try again.')

if 'n' in x1 and 'n' in x2 and y1 not in start_work and y2 not in leave_time:
    print('Is this even possible? We can\'t be hiring this person!')
else:
    pass
