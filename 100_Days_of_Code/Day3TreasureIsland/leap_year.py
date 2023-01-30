print("Leap Year Program.\n")

year = int(input("What year to check?\n"))

#if year % 4 == 0:
#  if year % 100 == 0:
#    if year % 400 == 0:
#      print(f"{year} is a Leap Year!")
#    else:
#      print(f"{year} is Not a Leap Year....")
#  else:
#    print(f"{year} is a Leap Year....")
#else:
#  print(f"{year} is Not a Leap Year....")
  
if year % 100 == 0:
  if year % 400 == 0:
    print(f"{year} is a Leap Year!")
  else:
    print(f"{year} is Not a Leap Year....")
elif year % 4 == 0:
    print(f"{year} is a Leap Year!")
else:
  print(f"{year} is Not a Leap Year....")