# row1 = ["⬜️","️⬜️","️⬜️","️⬜️","️⬜️","️⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","️⬜️","️⬜️","️⬜️","️⬜️","️⬜️","️⬜️","️⬜️"]
# row3 = ["⬜️","️⬜️","️⬜️","️⬜️","️⬜️","️⬜️","️⬜️","️⬜️"]
# row4 = ["⬜️","️⬜️","️⬜️","️⬜️","️⬜️","️⬜️","️⬜️","️⬜️"]
# row5 = ["⬜️","️⬜️","️⬜️","️⬜️","️⬜️","️⬜️","️⬜️","️⬜️"]
# row6 = ["⬜️","️⬜️","️⬜️","️⬜️","️⬜️","️⬜️","️⬜️","️⬜️"]
# row7 = ["⬜️","️⬜️","️⬜️","️⬜️","️⬜️","️⬜️","️⬜️","️⬜️"]
# row8 = ["⬜️","️⬜️","️⬜️","️⬜️","️⬜️","️⬜️","️⬜️","️⬜️"]
# map = [row1, row2, row3, row4, row5, row6, row7, row8]
# print(f"{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}")
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

column = int(position[0])
print(column)
row = int(position[1])

map[row - 1][column - 1] = " X"

print(f"{row1}\n{row2}\n{row3}")
# print(f"{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}")