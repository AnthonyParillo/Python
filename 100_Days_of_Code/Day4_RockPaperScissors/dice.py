import random

color = ["red","blue","green","yellow","purple","black"]
dice1 = random.randint(1,6)
shuffle_list = random.shuffle(color)
dice2 = random.choice(color)

print(dice1)
print(dice2)