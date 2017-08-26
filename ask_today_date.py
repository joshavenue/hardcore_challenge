from datetime import datetime

date_now = datetime.now()

num1 = input('What is the date day today? : ')
num2 = input('What is the month? : ')
num3 = input('What is the year? : ')

if num1 == date_now.day:
    pass
else:
    print 'Wrong day'

if num2 == date_now.month:
    pass
else:
    print 'Wrong month'

if num3 == date_now.year:
    pass
else:
    print 'Wrong year'

if num1 == date_now.day and num2 == date_now.month and num3 == date_now.year:
    print 'You do know the date!'
else:
    print 'Forget about the date?'
