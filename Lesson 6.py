import datetime
Password = 'Do it!'
user = input('Enter the password:')
while user != Password:
    print('Wrong password!')
    user = input('Enter the password:')
else:
    print ('Login successful!')