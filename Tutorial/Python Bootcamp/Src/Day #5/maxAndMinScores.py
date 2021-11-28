scores = input("Input a list of student scores: ").split()

#convert to list of int
for i in range(0, len(scores)):
    scores[i] = int(scores[i])


#SOLUTION 1
maxValue = 0
minValue = 0
for s in scores:
    if s > maxValue:
        maxValue = s
    if s < minValue:
        minValue = s
print(f"The Max score is {maxValue}, The Min score is {minValue}")

#SOLUTION 2
maxValue = max(scores)
minValue = min(scores)
print(f"The Max score is {maxValue}, The Min score is {minValue}")