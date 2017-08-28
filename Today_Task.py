from datetime import datetime
to_do_list = []
day_now = datetime.now()

def get_help():
    print('Type \'DONE\' when you are done.')
    print('Type \'CLEAN\' when you want to choose again.')
    print('Type \'HELP\' when you need help.')
    print('Type \'SHOW\' when you need to check your list.')

def clean_up():
    del to_do_list[:]

def show_list():
    print('Here are your task lists.')
    for list in to_do_list:
        print(list)

def show_list_END():
    print('You have {} tasks todays. Below are your tasks.'.format(len(to_do_list)))
    for list in to_do_list:
        print(list)

print('Today is {} / {} / {}'.format(day_now.day,day_now.month,day_now.year))
print('What should you for today?')
print('Enter \'DONE\' when you are done.')

while True:
    print('You have {} tasks in your list.'.format(len(to_do_list)))
    new_list = input(' > ')

    if new_list.lower() == 'DONE'.lower():
        break
    elif new_list.lower() == 'CLEAN'.lower():
        clean_up()
        continue
    elif new_list.lower() == "HELP".lower():
        get_help()
        continue
    elif new_list.lower() == 'SHOW'.lower():
        show_list()
        continue
    else:
        to_do_list.append(new_list)

show_list_END()
