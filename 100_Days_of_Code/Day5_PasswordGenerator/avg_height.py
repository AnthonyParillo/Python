# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights with spaces ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

tt_height = 0
for height in student_heights:
  tt_height += height
print(tt_height)

tt_students = 0
for student in student_heights:
  tt_students += 1
print(tt_students)

avg = round(tt_height / tt_students)

print(avg)