print("Welcome to Python's Pizza Deliveries!\n")

small = 15
medium = 20
large = 25
pepperoni_s = 2
pepperoni_ml = 3
cheese = 1
bill = 0

# Size
while True:
  size = input("What size would you like? S, M, L?: ")
  if size == "S":
    bill += small
    break
  elif size == "M":
    bill += medium
    break
  elif size == "L":
    bill += large
    break
  else:
    print("Type capital letters only. S, M, L")

# Pepperoni
while True:
  add_pepperoni = input("Would you like to add pepperoni? Y or N: ")
  if add_pepperoni == "Y":
    if size == "S":
      bill += pepperoni_s
    elif size == "M" or "L":
      bill += pepperoni_ml
    break
  elif add_pepperoni == "N":
    break
  else:
    print("Type capital letters only. Y or N")

# Extra Cheese
while True:
  extra_cheese = input("What about extra cheese? Y or N: ")
  if extra_cheese == "Y":
    bill += cheese
    break
  elif extra_cheese == "N":
    break
  else:
    print("Type capital letters only. Y or N")

print(f"Your final bill is: ${bill}")