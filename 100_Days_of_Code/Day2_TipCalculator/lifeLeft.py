age = int(input("What is your age?\n"))

last_age = 80
age_d = age * 365
age_w = age * 52
age_m = age * 12

remain_d = last_age * 365 - age_d
remain_w = last_age * 52 - age_w
remain_m = last_age * 12 - age_m

print(f"You have {remain_d} days, {remain_w} weeks, and {remain_m} months left")