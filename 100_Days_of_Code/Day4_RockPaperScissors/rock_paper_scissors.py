import random

# Welcome
print('Welcome to Rock, Paper, Scissors!!!\n')

# Description
print('Each person picks "rock", "paper", or "scissors".')

# List options
options = ["rock","paper","scissors"]

# Input choice

# Player 1
while True:
  player1 = input('\nPlayer 1\'s Choice: ')
  if player1 in options:
    break
  else:
    print('\nPlease choose words in quotations')
    continue
# Player 2
while True:
  player2 = input('\nPlayer 2\'s Choice: ')
  if player2 in options:
    break
  else:
    print('\nPlease choose words in quotations')
    continue
# Computer
# computer = random.choice(options)


# Logic
if player1 == options[0] and player2 == options[2]:
  print('\nPlayer 1 wins')
elif player1 == options[1] and player2 == options[0]:
  print('\nPlayer 1 wins')
elif player1 == options[2] and player2 == options[1]:
  print('\nPlayer 1 wins')
elif player1 == player2:
  print('\nTie!!!')
# elif player1 < computer:
#    print('Player 1 loses')
else:
  print('\nPlayer 2 wins!!')