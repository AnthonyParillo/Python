print("Welcome to the tip caluclator!\n")

bill_total = input("What is the total bill?\n$")
tip_total = input("How much percent(i.e. 15%) of tip do you want to give?\n")
ppl_total = input("How many people are paying?\n")

tip = (float(tip_total) / 100) + 1
after_tip_total = float(bill_total) * tip
each_person = format(after_tip_total / float(ppl_total),".2f")

print(f'Each person pays: ${each_person}')