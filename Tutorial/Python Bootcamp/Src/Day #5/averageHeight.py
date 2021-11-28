students_height = input("input a list of student heights: ")
students_height = students_height.split()

#SOLUTION 1
idx = 0
average_heigth = 0
for h in students_height:
    students_height[idx] = int(h)
    average_heigth += students_height[idx]
    idx += 1
average_heigth /= idx
print(f"Average height is {average_heigth}")

#SOLUTION 2
for idx in range(0, len(students_height)):
    students_height[idx] = int( students_height[idx] )
average_heigth = sum(students_height)/len(students_height)
print(f"Average height is {average_heigth}")

#SOLUTION 3
average_heigth = 0
for h in students_height:
    average_heigth += int(h)
average_heigth /= len(students_height)
print(f"Average height is {average_heigth}")