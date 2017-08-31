import os

def os_clear():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')
    else:
        pass

os_clear()

print('You are planning to do a maintainance on a vending machine.')
vending_machine = []
print('Type \'DONE\' when you are finished.')

while True:

    drink_name = input('What to stock up today? : ')
    vending_machine.append(drink_name)

    if drink_name.lower() == 'done':
        vending_machine.remove('done')
        break
    else:
        pass


os_clear()

print('You have : {}'.format(vending_machine))

while True:
    drink_name_y = input('What to remove today? : ')

    if drink_name_y.lower() in vending_machine:
        vending_machine.remove(drink_name_y)
        continue
    elif drink_name_y.lower() == 'done':
        break
    elif drink_name_y.lower() not in vending_machine:
        print('{} is not in the vending machine.'.format(drink_name_y))
    else:
        raise SystemExit
        
os_clear()


print('What is left in the vending machine : {}'.format(vending_machine))
