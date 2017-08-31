import numpy as np
import random
import os

def os_clear():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')
    else:
        pass

try:
    ask_dimension = int(input('How many dimension should a matrix has : '))
    if ask_dimension == 2:
        x_origin = int(input('Enter your starting number : '))
        x_end = int(input('Enter your final number : '))
        x_division = int(input('Enter your division power : '))

        if x_origin > x_end:
            print('{} is higher than {}, which is the end point.'.format(x1_origin,x1_end))
            raise SystemExit
        elif x_division > x_end:
            print('This won\'t work.')
            raise SystemExit
        elif x_division < x_origin:
            print('Won\'t work.')
            raise SystemExit
        else:
            pass

            temp = x_end / x_division

        try:
            shape_x = int(input('Enter the x-axis size : '))
            shape_y = int(input('Enter the y-axis size : '))

            if (shape_x * shape_y) < temp:
                print('Matrix invalid.')
            elif (shape_x * shape_y) == temp and x_origin < x_end:
                os_clear()
                print('Your matrix is now : \n ')
                print(np.arange(x_origin,x_end,x_division).reshape(shape_x,shape_y))
            else:
                os_clear()
                print(np.arange(x_origin,x_end,x_division).reshape(shape_x,shape_y))
                print('Invalid shape dimension.')
                raise SystemExit

        except ValueError:
            print('Invalid shape dimension.')
            raise SystemExit
    else:
        print('None other than 2D.')
except ValueError:
    print('Invalid dimension.')
    raise SystemExit
else:
    pass
