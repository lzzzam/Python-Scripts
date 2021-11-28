row1 = ["🙂", "🙂", "🙂"]
row2 = ["🙂", "🙂", "🙂"]
row3 = ["🙂", "🙂", "🙂"]

matrix = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}\n")

coordinates = input("Which coordinate you want to put an 'X' ? ==> ")

row = int(coordinates[0])
column = int(coordinates[1])

matrix[row][column] = 'X'

print(f"{row1}\n{row2}\n{row3}\n")