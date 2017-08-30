from datetime import datetime

day_now = datetime.now()
print('Today is {} / {} / {}'.format(day_now.day,day_now.month,day_now.year))

def ask():
    x = str(input('Enter your name \n Name : '))

    if x.isdigit():
        print('Only letters are accepted.')
    else:
        pass

        try:
            y = int(input('Enter your age \n Age : '))
        except ValueError:
            print('Age should be numbers.')
            raise SystemExit
        else:
            pass

        try:
            z = int(input('What year are you thinking? \n Year :'))
            if z < (day_now.year - y):
                print('You are not born yet.')
                raise SystemExit
            else:
                pass
        except ValueError:
            print('Numbers only.')
        else:
            pass

            year_difference = z - day_now.year
            age_future = year_difference + y

            if age_future > 80:
                print('You are probably not around anymore. If you are, you are {} years old.'.format(age_future))
            else:
                print('{} will be {} years old by the year {}.'.format(x,age_future,z))

ask()
