import random
List = ['Rock','Paper','Scissors']
print ('Welcome to Rock,Paper,and Scissors Game!')
print ('Choose one of the options:')
print (f'1 - {List[0]} \n 2 - {List[1]} \n3 - {List[2]}')
user = int(input('Your choice(Enter a number from 1 to 3):'))
user = List [user - 1]
print ('Your choice: ' + str(user))


bot = random.randint(1,3)
bot = List[bot - 1]
print ('Bots choice: ' + str(bot))


if user == bot:
   print ('Its a Draw!')
elif (user == 'Rock' and bot == 'Scissors') or \
   (user == 'Scissors' and bot == 'Paper') or \
   (user == 'Paper' and bot == 'Rock') :
   print ('You won!')
else:
   print ('You lost!')
