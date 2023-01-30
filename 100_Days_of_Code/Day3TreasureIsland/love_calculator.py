print("Welcome to the TRUE LOVE calculator!\n")

# List of TRUE and LOVE
true_list = ["t", "r", "u", "e"]
love_list = ["l", "o", "v", "e"]

# INPUT of Names
person1_fname = input("What is your first name?\n")
person1_lname = input("What is your last name?\n")
person2_fname = input("What is your lovers first name?\n")
person2_lname = input("What is your lovers name?\n")

# Concat names
per1_concat = str(person1_fname) + str(person1_lname)
per2_concat = str(person2_fname) + str(person2_lname)

# Make lower-case
lowerper1 = per1_concat.lower()
lowerper2 = per2_concat.lower()

# Count names with TRUE
count_true = sum(map(lowerper1.count, true_list)) + sum(map(lowerper2.count, true_list))

# Count names with LOVE
count_love = sum(map(lowerper1.count, love_list)) + sum(map(lowerper2.count, love_list))

print(f"Your percent is: {str(count_true) + str(count_love)}%")

# Change Str to Int
count_to_int = int(str(count_true) + str(count_love))

# Print Statements

if count_to_int < 40:
  print(f"Your score is {count_to_int}%, you go together like coke and mentos.")

elif count_to_int >= 40 and count_to_int <= 50:
  print(f"Your score is {count_to_int}%, you are alright together.")

elif count_to_int >= 80:
  print(f"Your score is {count_to_int}%, you are Amazing!! together.")
else:
  print(f"Your score is {count_to_int}%.")