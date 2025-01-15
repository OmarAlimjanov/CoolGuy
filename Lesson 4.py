# Chapters 1-2
# password = '2424'
# User = input('Enter your password: ')
# if User == password:
#     print('Login successful')
# if User != password:
#     print('Invalid password')

# Chapter 3
import datetime
name = input('What is your name? ')
print(f'Hello, {name} How can I help you?')
print('0 - Find out the time')
print('1 - Find out the date')
answer = int(input('How can I help you? '))
date_time = datetime.datetime.now()
if answer == 0:
    print('Current time:', date_time.time())
if answer == 1:
    print('Current date:', date_time.date())





