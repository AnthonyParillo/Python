import random
from random import shuffle
# Welcome
print('Welcome to Banker Roulette!')
print('\nWe will see who pays the bill today.')
# List
people = []
# How Many People
total = int(input('\nHow many People?:\n'))
# Add to List input
for i in range(total):
  whos_here = input('\nWho is here today?\n')
  people.append(whos_here)
# Shuffle
  shuffle(people)
# Random
who_pays = random.choice(people)
# Print
print(f'\nThe person who pays today is: {who_pays}')