name1 = input("Input Your Name: ").lower()
name2 = input("Input the name of your loved's one: ").lower()
coupleName = name1 + name2

loveString = "true love"

score = 0

for c in loveString:
    score += coupleName.count(c)

print(f"Your score is {score}")

if score < 10 or score > 90:
    print("Your are compatible like coca and soda")
elif score > 40 and score < 60:
    print("You're very compatible")
else:
    print("Not so bad")
