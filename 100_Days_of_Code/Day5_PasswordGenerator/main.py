high_score = input("Input a list of scores with spaces ").split()
for n in range(0, len(high_score)):
  high_score[n] = int(high_score[n])
print(high_score)

for h in high_score:
  if h > 